from PIL import Image
import os
import sys

print(sys.argv)
if (len(sys.argv) == 1):
    print("Enter file name!")
    quit(0)

image_src = str(sys.argv[1])
# image_src = '/home/hardik/Projects/Python-Stuff/dmssux/original/12.png'
white_threshold = 200
transparency_threshold = 160
count = 1

def conver_to_grayscale(file):
    img_buffer = Image.open(file).convert('LA')
    img_buffer.save('temp.png')

# source image is 100x30
# we trim out 3 px worth border from all sides
def remove_border(file):
    img_buffer = Image.open(file)
    cropped = img_buffer.crop((3, 3, 97, 27))
    cropped.save('temp.png')

def improve_color(file):
    img_buffer = Image.open(file)
    width, height = img_buffer.size
    for x in range(0, width):
        for y in range(0, height):
            darkness = img_buffer.getpixel((x, y))[0]
            if (darkness < white_threshold) :
                img_buffer.putpixel((x, y), (0, 255))
            else :
                img_buffer.putpixel((x, y), (0, 0))
    img_buffer.save('temp.png')

def strip_image(file, savefilename):
    img_buffer = Image.open(file)
    width, height = img_buffer.size
    left = 0
    top = 0
    right = 0
    bottom = 0
    # left
    for x in range(0, width):
        for y in range(0, height):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                left = x
                break
        if (hit == True):
            break

    # right
    for x in range(width - 1, 0, -1):
        for y in range(0, height):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                right = x + 1
                break
        if (hit == True):
            break

    # top
    for y in range(0, height):
        for x in range(0, width):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                top = y
                break
        if (hit == True):
            break
    
    # bottom
    for y in range(height - 1, 0, -1):
        for x in range(0, width):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                bottom = y + 1
                break
        if (hit == True):
            break
    # print(left, top, right, bottom)
    cropped = img_buffer.crop((left, top, right, bottom))
    cropped.save(savefilename)

def strip_image_image(img_buffer):
    width, height = img_buffer.size
    left = 0
    top = 0
    right = 0
    bottom = 0
    # left
    for x in range(0, width):
        for y in range(0, height):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                left = x
                break
        if (hit == True):
            break

    # right
    for x in range(width - 1, 0, -1):
        for y in range(0, height):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                right = x + 1
                break
        if (hit == True):
            break

    # top
    for y in range(0, height):
        for x in range(0, width):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                top = y
                break
        if (hit == True):
            break
    
    # bottom
    for y in range(height - 1, 0, -1):
        for x in range(0, width):
            hit = False
            pixel = img_buffer.getpixel((x, y))
            if (pixel[1] == 255):
                hit = True
                bottom = y + 1
                break
        if (hit == True):
            break
    # print(left, top, right, bottom)
    cropped = img_buffer.crop((left, top, right, bottom))
    return cropped

def shear_image(file):
    img = Image.open(file)
    width, height = img.size
    m = -0.35
    xshift = abs(m) * width
    # new_width = width + int(round(xshift))
    img = img.transform((width, height), Image.AFFINE, (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
    img.save('temp.png')

def improve_color_sheared(file):
    img_buffer = Image.open(file)
    width, height = img_buffer.size
    for x in range(0, width):
        for y in range(0, height):
            darkness = img_buffer.getpixel((x, y))[1]
            if (darkness > transparency_threshold) :
                img_buffer.putpixel((x, y), (0, 255))
            else :
                img_buffer.putpixel((x, y), (0, 0))
    img_buffer.save('temp.png')

def is_line_empty(img, x):
    h = img.size[1]
    for y in range(0, h):
        px = img.getpixel((x, y))[1]
        if (px == 255):
            return False
    return True

def separate_chars(file):
    img_buffer = Image.open(file)
    width, height = img_buffer.size
    x = 0
    global count
    while True:
        if (x == width):
            cropped = img_buffer.crop((0, 0, x, height))
            cropped.save(str(count) + '.png')
            break

        if (is_line_empty(img_buffer, x) == True):
            cropped = img_buffer.crop((0, 0, x, height))
            cropped.save(str(count) + '.png')
            count = count + 1
            img_buffer = strip_image_image(img_buffer.crop((x, 0, width, height)))
            width, height = img_buffer.size
            x = 0
        else:
            x = x + 1
    

while (count != 6):
    print(count)
    count = 1
    conver_to_grayscale(image_src)
    remove_border('temp.png')
    improve_color('temp.png')
    strip_image('temp.png', 'temp.png')
    shear_image('temp.png')
    improve_color_sheared('temp.png')
    strip_image('temp.png', 'temp.png')
    separate_chars('temp.png')
    white_threshold = white_threshold - 2
    transparency_threshold = transparency_threshold - 1
os.remove('temp.png')