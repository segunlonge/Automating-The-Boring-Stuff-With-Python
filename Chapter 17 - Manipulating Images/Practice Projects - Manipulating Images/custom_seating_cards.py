import os
from PIL import Image
from PIL import ImageDraw

from PIL import Image

path = os.getcwd()
with open(path+'\guests.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    guest_list = lines
    #print(guest_list)

    for guestname in guest_list:
        im = Image.new('RGBA', (288,360), 'white')
        width, height = im.size
        os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 17 - Manipulating Images\\Practice Projects - Manipulating Images')
        imflower = Image.open('flower.png')
        fwidth, fheight = imflower.size
        imflower = imflower.resize((fwidth//4,fheight//4))
        fwidth, fheight = imflower.size
        im.paste(imflower,(width//2-fwidth//2,height//2),imflower)

        I1 = ImageDraw.Draw(im)
        w, h = I1.textsize(guestname)
        I1.text(((width-w)/2, (height-h)/2),guestname, fill="black")
        
        im.save(guestname+'.png')

