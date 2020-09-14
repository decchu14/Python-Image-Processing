# this simple code is just to fetch the information of the image

from PIL import Image, ImageFilter

img = Image.open('pokedex/pikachu.jpg')

# will print the img object
print(img)

# will print the format of the img, jpeg,png, etc.
print(img.format)

# will print the size of the image, 640,640
print(img.size)

# will print the mode f the image, RGB
print(img.mode)

# for more methods run the below line of code
print(dir(img))
