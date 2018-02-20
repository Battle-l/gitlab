from PIL import Image, ImageDraw,ImageFont
import sys

base=Image.open(sys.argv[1]).convert('RGBA')
b_x,b_y = base.size
txt = Image.new('RGBA', (b_x+10,b_y+10),(255,255,255,255))
txt.paste(base,box=(0,10))
fnt = ImageFont.truetype('arial.ttf',20)
d=ImageDraw.Draw(txt)

d.text((b_x-5,0),'5',font=fnt,fill=(220,20,60,255))


txt.show()