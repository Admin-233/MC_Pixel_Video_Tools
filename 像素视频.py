#coding=utf-8
import sys
import os

from PIL import Image
import time

MAX_LEN =150
FIX_RATE = 2.7
REPLACEMENT = '     .,/*^!@#$%&()'


def convert(filename, max_len=MAX_LEN, fix_rate=FIX_RATE):
    image = Image.open(filename)
    image = image.convert('L')  

    width, height = image.size
    rate = max_len / max(width, height)
    width = int(rate * width)
    height = int(rate * height / fix_rate)

    image = image.resize((width,height))

    data = image.load()

    output = ''

    for h in range(height):
        for w in range(width):
            output += REPLACEMENT[int(data[w, h] / 256.0 * 16)]
    
        output += '\n'

    print(output)
times=1
amount=len(os.listdir("images"))
while times<=amount:
    convert("images/"+str(times)+".jpg")
    
    times=times+1
    time.sleep(0.01)
print("Video done.")
time.sleep(5)
