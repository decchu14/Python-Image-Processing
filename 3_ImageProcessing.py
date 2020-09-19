# this script compresses the given image without loosing quality and cropping the image
from PIL import Image, ImageFilter

img = Image.open("astro.jpg")
img.thumbnail((400, 400))
img.save('thumbnail.jpg')

# opens the img file on spot
img.show()

# cropping the img
img1 = Image.open("Pokedex/charmander.jpg")
box = (100, 100, 400, 400)
region = img1.crop(box)
region.save("cropped.png", 'png')
