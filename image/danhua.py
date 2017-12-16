#Thi program is to change every RGB color in each pixel
#I tried two lirbary two test, and look good

from PIL import Image,ImageDraw
im=Image.open('1.jpeg')
pix=im.load()

w,h=im.size
newIm=Image.new('RGB',(w,h),'white')
draw=ImageDraw.Draw(newIm)
testim=Image.new('RGB',(w,h),'white')
for x in range(w):
	for y in range(h):
		r,g,b=pix[x,y]
		draw.point((x,y),fill=(r//2,g//2,b//2))
		testim.putpixel((x,y),(r//2,g//2,b//2))
		print(r,g,b)
newIm.save('ImageDraw_test.bmp')
testim.save('usingPutPixel.bmp')
print(245//2)
