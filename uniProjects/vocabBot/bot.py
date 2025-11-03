import requests
import asyncio
import logging
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime
import time

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# DIRECT CONFIGURATION - UPDATE THESE VALUES!
# DIRECT CONFIGURATION - UPDATE THESE VALUES!
TELEGRAM_BOT_TOKEN = "8239632344:AAGwMM3L0JTdB0JnGyRgE8U02GLjdzBEgEM"
GROUP_CHAT_ID = "-1001821310406"  # Make sure this is correct
API_URL = "https://variabletribe.com/wp-json/vocab-bot/v1/daily"


print("🚀 Starting Vocabulary Telegram Bot...")
print("=" * 50)

class VocabularyBot:
    def __init__(self):
        print("🤖 Initializing Vocabulary Bot...")
        print(f"📝 Token: {TELEGRAM_BOT_TOKEN[:10]}...")
        print(f"👥 Group ID: {GROUP_CHAT_ID}")
        print(f"🌐 API URL: {API_URL}")
        
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
        
    async def initialize(self):
        """Initialize the bot with async connection test"""
        try:
            bot_info = await self.bot.get_me()
            print(f"✅ Bot connected: {bot_info.first_name} (@{bot_info.username})")
            return True
        except Exception as e:
            print(f"❌ Failed to connect to Telegram: {e}")
            return False
        
    def fetch_daily_vocabulary(self):
        """Fetch daily vocabulary from WordPress API (synchronous)"""
        try:
            print("🌐 Fetching vocabulary from API...")
            response = requests.get(API_URL, timeout=30)
            response.raise_for_status()
            data = response.json()
            print(f"✅ Successfully fetched: {data.get('word')}")
            return data
        except Exception as e:
            print(f"❌ Error fetching vocabulary: {e}")
            return None
    
    def format_telegram_message(self, vocab_data):
        """Format the vocabulary data into a nice Telegram message"""
        if not vocab_data:
            return "❌ Sorry, I couldn't fetch today's vocabulary. Please try again later."
        
        word = vocab_data.get('word', 'Unknown Word')
        meaning = vocab_data.get('meaning', '')
        part_of_speech = vocab_data.get('part_of_speech', [])
        examples = vocab_data.get('examples', [])
        pronunciation = vocab_data.get('pronunciation', {})
        categories = vocab_data.get('categories', [])
        
        # Build the message with emojis and formatting
        message = "📚 *Daily Vocabulary Word* 📚\n\n"
        
        # Word and pronunciation
        message += f"🔤 *Word*: {word}\n"
        
        if pronunciation.get('uk') or pronunciation.get('us'):
            message += "🔊 *Pronunciation*:\n"
            if pronunciation.get('uk'):
                message += f"   🇬🇧 UK: {pronunciation['uk']}\n"
            if pronunciation.get('us'):
                message += f"   🇺🇸 US: {pronunciation['us']}\n"
        
        # Part of speech
        if part_of_speech:
            pos_str = ", ".join([pos.capitalize() for pos in part_of_speech])
            message += f"📖 *Part of Speech*: {pos_str}\n"
        
        # Meaning
        if meaning:
            # Clean up the meaning format
            meaning_clean = meaning.replace('\r\n', '\n').replace('(n) :', '**Noun:**').replace('(v) :', '**Verb:**')
            message += f"💡 *Meaning*:\n{meaning_clean}\n"
        
        # Examples
        if examples:
            message += f"\n📝 *Examples*:\n"
            for i, example in enumerate(examples, 1):
                # Clean up example format
                example_clean = example.replace('(n) :', '').replace('(v) :', '')
                message += f"{i}. {example_clean}\n"
        
        # Categories
        if categories:
            message += f"\n🏷️ *Categories*: {', '.join(categories)}\n"
        
        # Footer with date and hashtag
        message += f"\n📅 *Date*: {datetime.now().strftime('%B %d, %Y')}\n"
        message += f"#Vocabulary #LearnEnglish #WordOfTheDay\n"
        message += f"#{word.replace(' ', '').replace('-', '').lower()}"
        
        return message
    
    async def send_message(self, message):
        """Send message to Telegram group (async)"""
        try:
            await self.bot.send_message(
                chat_id=GROUP_CHAT_ID,
                text=message,
                parse_mode='Markdown',
                disable_web_page_preview=True
            )
            print("✅ Message sent successfully to Telegram!")
            return True
        except TelegramError as e:
            print(f"❌ Telegram error: {e}")
            return False
    
    async def test_bot(self):
        """Test the bot functionality (async)"""
        print("\n" + "="*50)
        print("🧪 STARTING BOT TEST")
        print("="*50)
        
        # Test 1: Fetch vocabulary
        vocab_data = self.fetch_daily_vocabulary()
        
        if not vocab_data:
            print("❌ TEST FAILED: Could not fetch vocabulary data")
            return False
            
        print(f"✅ API Test Passed - Word: {vocab_data.get('word')}")
        
        # Test 2: Format message
        message = self.format_telegram_message(vocab_data)
        print("✅ Message formatting test passed")
        
        # Test 3: Send message
        print("📤 Sending test message to Telegram...")
        success = await self.send_message(message)
        
        if success:
            print("🎉 ALL TESTS PASSED! Bot is working correctly.")
            return True
        else:
            print("❌ TEST FAILED: Could not send message to Telegram")
            return False
    
    async def send_daily_vocab(self):
        """Send daily vocabulary (async)"""
        print(f"\n🔄 [{datetime.now().strftime('%H:%M:%S')}] Sending daily vocabulary...")
        vocab_data = self.fetch_daily_vocabulary()
        
        if vocab_data:
            message = self.format_telegram_message(vocab_data)
            await self.send_message(message)
            print(f"✅ Daily vocabulary sent: {vocab_data.get('word')}")
        else:
            error_msg = "❌ *Vocabulary Update Failed*\n\nSorry, I couldn't fetch today's vocabulary word. Please try again later."
            await self.send_message(error_msg)
            print("❌ Failed to send daily vocabulary")

async def main():
    try:
        # Create bot instance
        bot = VocabularyBot()
        
        # Initialize bot (async)
        connected = await bot.initialize()
        if not connected:
            return
        
        # Test the bot first
        print("\n🧪 Testing bot connection...")
        success = await bot.test_bot()
        
        if success:
            print("\n🎊 Congratulations! Your bot is working!")
            
            # Ask if user wants to start sending messages
            print("\nDo you want to send messages immediately? (y/n): ")
            # For async, we'll just send one message for now
            await bot.send_daily_vocab()
            
            print("\n✅ Bot test completed successfully!")
            print("\nTo run this bot 24/7, you need to:")
            print("1. Deploy to a cloud server (PythonAnywhere, Heroku, etc.)")
            print("2. Use a proper task scheduler")
            print("3. Run this script periodically using cron jobs or similar")
            
        else:
            print("\n❌ Bot test failed. Please check the errors above.")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")

def run_bot():
    """Run the bot using asyncio"""
    asyncio.run(main())

if __name__ == "__main__":
    run_bot()