from sys import argv
import os
from PIL import Image

# grabing first and second arguements from commandline
jpg_folder = argv[1]
png_folder = argv[2]

# checking whether folder exists if not creating
if not os.path.exists(png_folder):
    os.mkdir(png_folder)

# path of the folder which contains jpg images
directory = f'path/{jpg_folder}'

# looping through folder and converting images to png and saving it in another folder
for filename in os.listdir(directory):
    img = Image.open(f'{directory}/{filename}')
    # splitting the name from its extension
    filename_without_ext = os.path.splitext(filename)[0]
    # new_filename = f'{filename_without_ext}.png'
    img.save(f'{png_folder}/{filename_without_ext}.png', 'png')
