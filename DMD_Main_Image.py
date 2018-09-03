import os
from PIL import Image, ImageDraw

img = Image.new("RGB", (1024, 768), "white")
img.save(os.getcwd() + '/white.png')

# img.show(main_img)
