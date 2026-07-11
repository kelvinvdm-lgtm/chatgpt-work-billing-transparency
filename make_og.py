from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
W,H=1200,630
img=Image.new('RGB',(W,H),(8,11,18))
d=ImageDraw.Draw(img)
for y in range(H):
    t=y/H
    d.line((0,y,W,y),fill=(8+int(10*t),11+int(14*t),18+int(22*t)))
for x,y,r,c in [(110,70,260,(40,80,180)),(1080,110,290,(20,120,150)),(950,590,250,(120,70,30))]:
    layer=Image.new('RGBA',(W,H),(0,0,0,0));ld=ImageDraw.Draw(layer);ld.ellipse((x-r,y-r,x+r,y+r),fill=(*c,55));img=Image.alpha_composite(img.convert('RGBA'),layer)
d=ImageDraw.Draw(img)
def font(size,bold=False):
    paths=[r'C:\Windows\Fonts\seguisb.ttf' if bold else r'C:\Windows\Fonts\segoeui.ttf',r'C:\Windows\Fonts\arialbd.ttf' if bold else r'C:\Windows\Fonts\arial.ttf']
    for p in paths:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()
d.rounded_rectangle((60,50,430,98),24,outline=(78,231,255),width=2,fill=(12,20,31,220))
d.text((85,61),'INDEPENDENT BILLING REPORT',font=font(20,True),fill=(78,231,255))
d.text((60,155),'ChatGPT Work',font=font(74,True),fill=(244,247,251))
d.text((60,235),'and Codex share',font=font(74,True),fill=(244,247,251))
d.text((60,315),'one meter.',font=font(86,True),fill=(78,231,255))
d.rounded_rectangle((60,445,1140,560),22,fill=(17,23,34,235),outline=(40,52,72),width=2)
d.text((90,468),'Shared usage  •  Shared credits  •  Auto top-up exposure',font=font(30,True),fill=(255,204,102))
d.text((90,516),'Official OpenAI sources verified 11 July 2026',font=font(23),fill=(169,179,195))
img.convert('RGB').save(Path(__file__).with_name('og-card.png'),quality=95)
