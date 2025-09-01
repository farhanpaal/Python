import os
import logging
import json
import re
from typing import Dict, List, Optional
from uuid import uuid4
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    ContextTypes, filters, CallbackQueryHandler
)

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))

# Cache file to store book index
CACHE_FILE = "book_index.json"
CACHE_EXPIRY_HOURS = 24  # Refresh cache every 24 hours

# Initialize bot
class EbookFatherBot:
    def __init__(self):
        self.application = Application.builder().token(BOT_TOKEN).build()
        self.bot = self.application.bot
        self.book_cache = {}
        self.book_index = {}  # Local index: {message_id: {title, file_type, file_id}}
        self.last_cache_update = None
        self.setup_handlers()
        
        # Load index on initialization
        self.application.post_init = self.post_init
        
    async def post_init(self, application):
        """Load index after application is initialized"""
        await self.load_or_create_index()
    
    def setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("search", self.search_command))
        self.application.add_handler(CommandHandler("generate_link", self.generate_link_command))
        self.application.add_handler(CommandHandler("update_index", self.update_index_command))
        self.application.add_handler(CommandHandler("stats", self.stats_command))
        self.application.add_handler(CommandHandler("debug_detailed", self.debug_detailed_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(CallbackQueryHandler(self.button_callback))
        self.application.add_error_handler(self.error_handler)
    
    async def debug_detailed_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Detailed debug to see exactly what's in the channel"""
        await update.message.reply_text("🔍 Performing detailed channel scan...")
        
        try:
            # Test channel access first
            chat = await self.bot.get_chat(DATABASE_CHANNEL_ID)
            await update.message.reply_text(f"✅ Channel access: {chat.title}")
            
            message_count = 0
            file_count = 0
            detailed_results = ""
            
            # Scan the channel
            async for message in self.bot.get_chat_history(chat_id=DATABASE_CHANNEL_ID, limit=50):
                message_count += 1
                
                # Check message type
                message_type = "text"
                file_info = ""
                
                if message.document:
                    message_type = "document"
                    filename = getattr(message.document, 'file_name', 'No filename')
                    file_info = f"📄 Document: {filename}"
                elif message.video:
                    message_type = "video"
                    filename = getattr(message.video, 'file_name', 'No filename')
                    file_info = f"🎥 Video: {filename}"
                elif message.audio:
                    message_type = "audio"
                    filename = getattr(message.audio, 'file_name', 'No filename')
                    file_info = f"🎵 Audio: {filename}"
                elif message.photo:
                    message_type = "photo"
                    file_info = "🖼️ Photo"
                else:
                    message_type = "text/other"
                    if hasattr(message, 'text') and message.text:
                        file_info = f"📝 Text: {message.text[:50]}..."
                    else:
                        file_info = "❓ Unknown message type"
                
                # Check for caption
                caption = getattr(message, 'caption', 'No caption')
                
                # Count files
                if message_type in ['document', 'video', 'audio']:
                    file_count += 1
                    detailed_results += f"\n{file_count}. {file_info}\n   Caption: {caption}\n"
                
                # Stop after 20 files to avoid message limits
                if file_count >= 20:
                    break
            
            # Send results
            result_message = (
                f"📊 Detailed Channel Analysis:\n"
                f"Messages scanned: {message_count}\n"
                f"Files found: {file_count}\n\n"
            )
            
            if file_count > 0:
                result_message += "Files found:\n" + detailed_results
            else:
                result_message += (
                    "❌ No files found in the channel!\n\n"
                    "Possible reasons:\n"
                    "1. Bot doesn't have permission to read the channel\n"
                    "2. Channel ID is incorrect\n"
                    "3. Files are not documents/videos/audio\n"
                    "4. Channel is empty\n"
                    "5. Files are too old (bot scans recent messages first)"
                )
            
            await update.message.reply_text(result_message)
            
        except Exception as e:
            error_msg = (
                f"❌ Channel access error: {e}\n\n"
                "This usually means:\n"
                "1. Bot is not in the channel\n"
                "2. Channel ID is wrong\n"
                "3. Bot doesn't have read permissions"
            )
            await update.message.reply_text(error_msg)
    
    async def load_or_create_index(self):
        """Load existing index or create a new one"""
        try:
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, 'r') as f:
                    data = json.load(f)
                    self.book_index = data.get('book_index', {})
                    last_update_str = data.get('last_update', '')
                    if last_update_str:
                        self.last_cache_update = datetime.fromisoformat(last_update_str)
                    
                    # Check if cache is expired
                    if (self.last_cache_update and 
                        (datetime.now() - self.last_cache_update) > timedelta(hours=CACHE_EXPIRY_HOURS)):
                        await self.update_index()
            else:
                await self.update_index()
        except Exception as e:
            logging.error(f"Error loading index: {e}")
            await self.update_index()
    
    async def update_index(self):
        """Update the book index from the channel with detailed logging"""
        try:
            await self.log_action(None, "Starting detailed index update...")
            new_index = {}
            count = 0
            scanned_messages = 0
            
            # Scan channel for books with detailed logging
            async for message in self.bot.get_chat_history(chat_id=DATABASE_CHANNEL_ID, limit=200):
                scanned_messages += 1
                
                # Log progress every 50 messages
                if scanned_messages % 50 == 0:
                    await self.log_action(None, f"Scanned {scanned_messages} messages, found {count} books so far")
                
                # Check if message has a file
                has_file = message.document or message.video or message.audio
                if not has_file:
                    continue
                
                # Get book info with better error handling
                try:
                    caption = getattr(message, 'caption', '') or ''
                    filename = ''
                    
                    if message.document:
                        filename = getattr(message.document, 'file_name', '') or ''
                        file_id = message.document.file_id
                        file_type = 'document'
                    elif message.video:
                        filename = getattr(message.video, 'file_name', '') or ''
                        file_id = message.video.file_id
                        file_type = 'video'
                    elif message.audio:
                        filename = getattr(message.audio, 'file_name', '') or ''
                        file_id = message.audio.file_id
                        file_type = 'audio'
                    else:
                        continue
                    
                    # Add to index
                    title = caption or filename or 'Unknown Title'
                    new_index[message.message_id] = {
                        'title': title,
                        'file_type': file_type,
                        'file_id': file_id
                    }
                    count += 1
                    
                except Exception as e:
                    await self.log_action(None, f"Error processing message {message.message_id}: {e}")
                    continue
            
            # Update index and save to file
            self.book_index = new_index
            self.last_cache_update = datetime.now()
            
            # Save to file
            with open(CACHE_FILE, 'w') as f:
                json.dump({
                    'book_index': self.book_index,
                    'last_update': self.last_cache_update.isoformat()
                }, f)
            
            # Detailed result message
            result_msg = (
                f"Index update completed!\n"
                f"Scanned messages: {scanned_messages}\n"
                f"Books found: {count}\n"
            )
            
            if count > 0:
                result_msg += "First few books:\n"
                for i, (msg_id, book) in enumerate(list(self.book_index.items())[:5], 1):
                    result_msg += f"{i}. {book['title']}\n"
            else:
                result_msg += "❌ No books found. Check channel permissions and content."
            
            await self.log_action(None, result_msg)
            
        except Exception as e:
            error_msg = f"❌ Index update failed: {e}"
            logging.error(error_msg)
            await self.log_action(None, error_msg)
            
    async def update_index_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manually update the book index"""
        await update.message.reply_text("🔄 Updating book index... This may take a while.")
        await self.update_index()
        book_count = len(self.book_index)
        await update.message.reply_text(f"✅ Index updated! Now have {book_count} books in index.")
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show index statistics"""
        book_count = len(self.book_index)
        last_update = self.last_cache_update.strftime("%Y-%m-%d %H:%M") if self.last_cache_update else "Never"
        
        await update.message.reply_text(
            f"📊 Index Statistics:\n"
            f"• Books in index: {book_count}\n"
            f"• Last updated: {last_update}\n"
            f"• Use /update_index to refresh"
        )
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        welcome_message = (
            f"Hello {user.mention_html()}! 👋\n\n"
            "I'm <b>EbookFatherBot</b> 📚\n"
            "I can help you find ebooks from our collection.\n\n"
            "🔍 To search: Type book name or use /search\n"
            "Use /help for more commands."
        )
        
        await update.message.reply_html(welcome_message)
        await self.log_action(update, f"User {user.id} started the bot")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "<b>EbookFatherBot Help</b> 📚\n\n"
            "<b>Commands:</b>\n"
            "/start - Start the bot\n"
            "/help - Show this help message\n"
            "/search <book_name> - Search for a book\n"
            "/generate_link <book_name> - Generate shareable link\n"
            "/update_index - Update the book index\n"
            "/stats - Show index statistics\n\n"
            "<b>Usage:</b>\n"
            "Just type a book name to search for it!"
        )
        await update.message.reply_html(help_text)
    
    async def search_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Please specify a book name. Usage: /search <book_name>")
            return
        
        query = " ".join(context.args)
        await self.search_books(update, query)
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.message.text
        if query.strip() and not query.startswith('/'):
            await self.search_books(update, query)
    
    async def search_books(self, update: Update, query: str):
        await update.message.chat.send_action(action="typing")
        
        books = await self.find_books(query)
        
        if not books:
            await update.message.reply_text(
                f"❌ No books found matching '{query}'.\n\n"
                "Please try a different search term."
            )
            return
        
        if len(books) == 1:
            book = books[0]
            await self.send_book(update, book)
        else:
            keyboard = []
            for book in books:
                keyboard.append([InlineKeyboardButton(
                    book['title'][:50] + ("..." if len(book['title']) > 50 else ""), 
                    callback_data=f"book_{book['message_id']}"
                )])
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message极端的reply_text(
                f"📚 Found {len(books)} books matching '{query}':",
                reply_markup=reply_markup
            )
  
    async def find_books(self, query: str) -> List[Dict]:
        """Search for books in the local index."""
        books = []
        query = query.lower().strip()
        
        if not query or not self.book_index:
            return books
        
        try:
            for message_id, book_info in self.book極端index.items():
                title = book_info['title'].lower()
                
                # Multiple search strategies
                if (query in title or  # Exact substring match
                    any(word in title for word in query.split()) or  # Any word match
                    self.fuzzy_match(query, title)):  # Fuzzy matching
                    
                    books.append({
                        'title': book_info['title'],
                        'file_id': book_info['file_id'],
                        'message_id': message_id,
                        'file_type': book_info['file_type']
                    })
                
                if len(books) >= 15:  # Limit results
                    break
                    
        except Exception as e:
            logging.error(f"Error searching index: {e}")
        
        return books
    
    def fuzzy_match(self, query: str, text: str) -> bool:
        """Flexible matching for common variations."""
        # Remove special characters and extra spaces
        clean_query = re.sub(r'[^\w\s]', '', query).strip()
        clean_text = re.sub(r'[^\w\s]', '', text).strip()
        
        # Check if all query words appear in text (極端any order)
        query_words = clean_query.split()
        text_words = clean_text.split()
        
        return all(any(word in text_word for text_word in text_words) 
                   for word in query_words if len(word) > 2)

    async def send_book(self, update: Update, book: Dict, from_callback: bool = False):
        """Send a book to the user."""
        chat_id = update.callback_query.message.chat_id if from_callback else update.message.chat_id
        
        try:
            if book['file_type'] == 'document':
                await self.bot.send_document(
                    chat_id=chat_id, 
                    document=book['file_id'],
                    caption=f"📖 {book['title']}\n\nEnjoy your reading! 📚"
                )
            elif book['file_type'] == 'video':
                await self.bot.send_video(
                    chat_id=chat_id, 
                    video=book['file_id'],
                    caption=f"📖 {book['title']}\n\nEnjoy your reading! 📚"
                )
            elif book['file_type'] == 'audio':
                await self.bot.send_audio(
                    chat_id=chat_id, 
                    audio=book['file_id'],
                    caption=f"📖 {book['title']}\n\nEnjoy your reading! 📚"
                )
            
            # Log the book delivery
            user = update.effective_user
            await self.log_action(update, f"Sent book '{book['title']}' to user {user.id}")
            
            if from_callback:
                await update.callback_query.answer()
                
        except Exception as e:
            logging.error(f"Error sending book: {e}")
            error_msg = "❌ Sorry, I couldn't retrieve the book. Please try again later."
            
            if from_callback:
                await update.callback_query.answer(error_msg, show_alert=True)
            else:
                await update.message.reply_text(error_msg)
    
    async def generate_link_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Generate a shareable link for a book."""
        if not context.args:
            await update.message.reply_text("Please specify a book name. Usage: /generate_link <book_name>")
            return
        
        query = " ".join(context.args)
        await update.message.chat.send_action(action="typing")
        
        books = await self.find_books(query)
        
        if not books:
            await update.message.reply_text(f"❌ No books found matching '{query}'.")
            return
        
        if len(books) > 1:
            keyboard = []
            for book in books:
                keyboard.append([InlineKeyboardButton(
                    book['title'][:50] + ("..." if len(book['title']) > 50 else ""), 
                    callback_data=f"link_{book['message_id']}"
                )])
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                f"📚 Found {len(books)} books. Please select one to generate a link:",
                reply_markup=reply_markup
            )
        else:
            book = books[0]
            link = await self.generate_book_link(book['message_id'])
            await update.message.reply_text(f"🔗 Share this link: {link}")
    
    async def generate_book_link(self, message_id: int) -> str:
        """Generate a deep link for a specific book."""
        unique_id = str(uuid4())
        self.book_cache[unique_id] = message_id
        bot_username = (await self.bot.get_me()).username
        return f"https://t.me/{bot_username}?start=book_{unique_id}"
    
    async def get_book_from_index(self, message_id: int) -> Optional[Dict]:
        """Get book info from index by message ID."""
        book_info = self.book_index.get(message_id)
        if book_info:
            return {
                'title': book_info['title'],
                'file_id': book_info['file_id'],
                'message_id': message_id,
                'file_type': book_info['file_type']
            }
        return None
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button callbacks."""
        query = update.callback_query
        data = query.data
        
        if data.startswith("book_"):
            message_id = int(data[5:])
            book = await self.get_book_from_index(message_id)
            
            if book:
                await self.send_book(update, book, from_callback=True)
            else:
                await query.answer("❌ Book not available.", show_alert=True)
        
        elif data.startswith("link_"):
            message_id = int(data[5:])
            book = await self.get_book_from_index(message_id)
            
            if book:
                link = await self.generate_book_link(message_id)
                await query.edit_message_text(f"🔗 Share this link: {link}")
            else:
                await query.answer("❌ Book not available.", show_alert=True)
    
    async def log_action(self, update: Optional[Update], action: str):
        """Log actions to the log channel."""
        try:
            user_info = ""
            if update and update.effective_user:
                user = update.effective_user
                user_info = f"User: {user.id} (@{user.username})\n"
            
            log_message = f"{user_info}Action: {action}"
            await self.bot.send_message(chat_id=LOG_CHANNEL_ID, text=log_message)
        except Exception as e:
            logging.error(f"Error logging action: {e}")
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Log errors caused by updates."""
        logging.error(f"Exception while handling an update: {context.error}")
        try:
            error_message = f"❌ Error: {context.error}"
            await self.bot.send_message(chat_id=LOG_CHANNEL_ID, text=error_message)
        except Exception as e:
            logging.error(f"Error sending error to log channel: {e}")

def main():
    """Start the bot."""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    ebook_bot = EbookFatherBot()
    ebook_bot.application.run_polling()

if __name__ == '__main__':
    main()