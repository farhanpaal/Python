"""
This is a program where you can create a QR code for UPI payment.
It is simple code, but styling making it look complex for a beginner.

To use it- Install these two libraries:
1) pip install qrcode[pil] --> to generate the QR code
2) pip install pillow      --> A Python tool that helps you create, edit, and save images.

With pillow we can:
- Draw on images
- Write text on them
- Add effects like blur or glow
- Save the final result


"""

import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# === UPI Data ===
upi_id = "variabletribe@jkb"
payee_name = "Farhan Pala"
note = "Pay now"
upi_link = f"upi://pay?pa={upi_id}&pn={payee_name}&tn={note}&cu=INR"

# === Generate QR ===
qr = qrcode.make(upi_link).convert("RGBA")
qr_width, qr_height = qr.size

# === Canvas dimensions ===
margin = 80
header_height = 120
footer_height = 100
canvas_width = qr_width + margin * 2
canvas_height = qr_height + header_height + footer_height

# === Create dark blue-green-cyan aesthetic gradient ===
bg = Image.new("RGBA", (canvas_width, canvas_height))
draw = ImageDraw.Draw(bg)

start_color = (10, 40, 90)       # Deep blue top
mid_color = (10, 30, 70)        # Deep dark blue
end_color = (30, 60, 180)        # Rich royal blue bottom

for y in range(canvas_height):
    # Blend top → mid → bottom
    if y < canvas_height // 2:
        ratio = y / (canvas_height // 2)
        r = int(start_color[0] + (mid_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (mid_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (mid_color[2] - start_color[2]) * ratio)
    else:
        ratio = (y - canvas_height // 2) / (canvas_height // 2)
        r = int(mid_color[0] + (end_color[0] - mid_color[0]) * ratio)
        g = int(mid_color[1] + (end_color[1] - mid_color[1]) * ratio)
        b = int(mid_color[2] + (end_color[2] - mid_color[2]) * ratio)

    draw.line([(0, y), (canvas_width, y)], fill=(r, g, b))

# === Glass Card Layer behind QR ===
glass = Image.new("RGBA", (qr_width + 40, qr_height + 40), (255, 255, 255, 60))
glass = glass.filter(ImageFilter.GaussianBlur(radius=8))
bg.paste(glass, (margin - 20, header_height - 20), glass)

# === Paste QR Code ===
bg.paste(qr, (margin, header_height), qr)

# === Load Fonts ===
try:
    title_font = ImageFont.truetype("arial.ttf", 38)
    subtitle_font = ImageFont.truetype("arial.ttf", 22)
    quote_font = ImageFont.truetype("ariali.ttf", 20)  # italic
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    quote_font = ImageFont.load_default()

# === Draw Name ===
title_text = "Farhan Pala"
title_w = draw.textbbox((0, 0), title_text, font=title_font)[2]
draw.text(((canvas_width - title_w) // 2, 30), title_text, fill="white", font=title_font)

# === Draw Subheading ===
subtitle = "Scan and Pay"
sub_w = draw.textbbox((0, 0), subtitle, font=subtitle_font)[2]
draw.text(((canvas_width - sub_w) // 2, 75), subtitle, fill=(200, 200, 255), font=subtitle_font)

# === Draw Quote ===
quote = "Every transaction writes the next line of the story."
quote_w = draw.textbbox((0, 0), quote, font=quote_font)[2]
draw.text(((canvas_width - quote_w) // 2, header_height + qr_height + 40),
          quote, fill=(180, 220, 255), font=quote_font)

 
# === Save image ===
bg.save("farhanPala.png")
