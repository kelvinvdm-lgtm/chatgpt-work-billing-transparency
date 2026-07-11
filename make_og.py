from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

W, H = 1200, 630
img = Image.new('RGB', (W, H), (5, 8, 15))
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line((0, y, W, y), fill=(5 + int(10*t), 8 + int(16*t), 15 + int(24*t)))

# Atmospheric glows
for x, y, r, c in [(115, 75, 270, (30, 85, 210)), (1090, 150, 310, (10, 165, 185)), (960, 625, 300, (210, 105, 25))]:
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse((x-r, y-r, x+r, y+r), fill=(*c, 62))
    layer = layer.filter(ImageFilter.GaussianBlur(55))
    img = Image.alpha_composite(img.convert('RGBA'), layer)

d = ImageDraw.Draw(img)

def font(size, bold=False):
    paths = [r'C:\Windows\Fonts\seguisb.ttf' if bold else r'C:\Windows\Fonts\segoeui.ttf',
             r'C:\Windows\Fonts\arialbd.ttf' if bold else r'C:\Windows\Fonts\arial.ttf']
    for p in paths:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

# Header badge
d.rounded_rectangle((60, 45, 430, 98), 26, outline=(72, 235, 255), width=2, fill=(10, 18, 30, 225))
d.text((84, 60), 'PAID-POOL EVIDENCE REPORT', font=font(20, True), fill=(72, 235, 255))

# Main statement
d.text((60, 145), 'More paid products.', font=font(72, True), fill=(246, 249, 255))
d.text((60, 225), 'The same usage pool.', font=font(76, True), fill=(72, 235, 255))
d.text((60, 315), 'When one consumes it, less remains for the others.', font=font(34, True), fill=(255, 214, 118))

# Product chips
chips = [('WORK', 60), ('CODEX', 260), ('EXCEL', 470), ('AGENTS', 670)]
for label, x in chips:
    d.rounded_rectangle((x, 400, x+170, 455), 16, outline=(60, 79, 110), width=2, fill=(15, 24, 39, 235))
    tw = d.textbbox((0, 0), label, font=font(23, True))[2]
    d.text((x + (170-tw)/2, 414), label, font=font(23, True), fill=(230, 237, 249))

# Footer evidence line
d.rounded_rectangle((60, 495, 1140, 575), 20, fill=(14, 21, 33, 235), outline=(48, 63, 88), width=2)
d.text((88, 515), 'One paid-plan allowance  |  Shared credits  |  Users may also help improve models', font=font(25, True), fill=(192, 205, 225))
d.text((88, 548), 'Built with GPT-5.6 Thinking  |  Primary OpenAI sources verified 11 July 2026', font=font(18), fill=(143, 157, 180))

img.convert('RGB').save(Path(__file__).with_name('og-card.png'), quality=96)
