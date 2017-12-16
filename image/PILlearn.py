#This program is to compress the imgae into half size 


im=Image.open('1.jpeg')
w,h=im.size
print('Original image size %sx%s'%(w,h))
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s'%(w//2,h//2))
im.save('half1_.jpeg')

