#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 17 - Manipulating Images')

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((50,50))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.bmp')
            or filename.lower().endswith('.gif')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculated the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
        #im.save(os.path.join('withLogo', 'resized.png'))
        #logoIm.save(os.path.join('withLogo', 'logo.png'))

    # Add the logo.
    if logoWidth*2 <= width and logoHeight*2 <= height:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        # Save changes.
        im.save(os.path.join('withLogo', filename))
    else:
        print('Skip %s...' % (filename))


