import os
from PIL import Image

for file in os.listdir('Images'):
    img = Image.open('Images\\' + file)
    img.save('Images\\png\\' + file[:-4] + '.png', 'png')
