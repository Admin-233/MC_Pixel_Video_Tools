#coding=utf-8
import sys
import os
import keyboard
from PIL import Image
import time

MAX_LEN =95
FIX_RATE = 2.7
REPLACEMENT = '  111111111111111111111111111111111111111111111111111111'


def convert(filename, max_len=MAX_LEN, fix_rate=FIX_RATE):
    image = Image.open(filename)
    image = image.convert('L')

    width, height = image.size
    rate = max_len / max(width, height)
    width = int(rate * width)
    height = int(rate * height / fix_rate)

    image = image.resize((width, height))

    data = image.load()

    output = ''

    for h in range(height):
        for w in range(width):
            output += REPLACEMENT[int(data[w, h] / 256.0 * 16)]
        output += '\n'

    print("")
    print(output)

while True:
    convert("1.jpg")
    
    
    time.sleep(0.5)

