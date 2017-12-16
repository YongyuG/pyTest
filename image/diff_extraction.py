#This program is to extract the difference between two image
#We can say the difference is the feature

import matplotlib.pyplot as plt
from PIL import Image
img1=Image.open("1.jpeg")
img_array1=img1.load()
img2=Image.open("2.jpeg")
img_array2=img2.load()
im=Image.new("RGB",(512,512),"white")
img_array=im.load()

for i in range(1,512):
    for j in range(1,512):
        if img_array1[i,j] != img_array2[i,j]:
            img_array[i,j]=img_array2[i,j]

im.save('success.bmp')
