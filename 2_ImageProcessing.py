# this simple code is to filter or convert the image
from PIL import Image, ImageFilter
img = Image.open('pokedex/pikachu.jpg')

# will filter the image to blur or smooth or sharpen and store it in variable named filtered_img
filtered_image = img.filter(ImageFilter.BLUR)  # SMOOTH, SHARPEN

# will save the filtered_img in new file named blur.png as png format
# img can be found inside processed images folder
filtered_image.save("blur.png", "png")

# converts the img to black and white and store it in variable named fil_img
fil_img = img.convert('L')

# will save the fil_img in new file named grey.png as png format
# img can be found inside processed images folder
fil_img.save("grey.png", "png")

# rotates the image in 180 degree direction and saves it in grey.png file as png format
crooked = img.rotate(180)
crooked.save("grey.png", "png")

# resizes the image into given pixels(300,300) and saves it in file named grey.png as png format
resize = fil_img.resize((300, 300))
resize.save("grey.png", "png")
