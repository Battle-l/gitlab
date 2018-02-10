import os,sys
from PIL import Image, ImageFilter,ImageEnhance, PSDraw


def roll(image, delta):
	'''Roll an image sideways.'''
	xsize, ysize = image.size
	delta=delta%xsize
	mask=[100]
	if delta==0: return image
	
	part1 = image.crop((0,0,delta,ysize))
	part2 = image.crop((delta,0,xsize,ysize))
	part1.load()
	part2.load()
	image.paste(part2,(0,0,xsize-delta, ysize))
	image.paste(part1,(xsize-delta,0,xsize,ysize))
	
	return image

im = Image.open('Assassin.png')
title = 'Assassin'
box=(1*72,2*72,70*72,100*72)

ps = PSDraw.PSDraw('Assassin.png')
ps.begin_document(title)

ps.image(box,im,75)
ps.rectangle(box)

ps.setfont('HelveticaNarrow-Bold',72)
ps.text((3*72,4*72),title)

ps.end_document()
ps

