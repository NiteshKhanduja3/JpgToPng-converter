from PIL import Image,ImageFilter
img = Image.open('4.4 pikachu.jpg')


#bluring the image
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save("blur.png",'png')

#smoothing the image
filter_img1 = img.filter(ImageFilter.SMOOTH)
filter_img1.save("SmoothPikchu.png","png")

#sharpning the image
filter_img2 = img.filter(ImageFilter.SHARPEN)
filter_img2.save("SharpPikchu.png","png")

#converting the image scale(Doing  balck and white to an image)
filter_img3 = img.convert('L')
filter_img3.save("Black_And_WhitePikchu.png","png")
filter_img3.show() # showing the image


# rotating the existing image
rotated = filter_img1.rotate(90)
rotated.save("rotatedpikachu.png",'png')

# resize Images
resize= filter_img1.resize((300,300))
resize.save("Resizedpikachu.png",'png')

# cropping the Image
box =(100,100,400,400)
region = filter_img1.crop(box)
region.save("croppedpickachu",'png')


# Decrease the size of the Image
img1 = Image.open('highResolution.jpg')
new_img = img1.resize((400,400)) #Decrease the quality of an Image
new_img.save('smallImage.png','png')

#making Thumbnaile of the image
img1.thumbnail((400,400)) # does't decrease the quality
img1.save('thumbnail.jpg')

