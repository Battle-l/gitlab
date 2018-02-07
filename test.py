from PIL import Image, ImageDraw,ImageFont
import sys

base=Image.open('TIM.png').convert('RGBA')
txt = Image.new('RGBA', base.size,(255,255,255,0))

fnt = ImageFont.truetype('arial.ttf',40)
d=ImageDraw.Draw(txt)

d.text((10,10),'Hello',font=fnt,fill=(255,255,255,128))
d.text((10,60),'World',font=fnt,fill=(255,255,255,255))

out=Image.alpha_composite(base,txt)

out.show()

