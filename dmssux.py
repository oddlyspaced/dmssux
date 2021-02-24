from PIL import Image

image_src = '/home/hardik/Projects/Python-Stuff/dmssux/original/12.png'
white_threshold = 200

def conver_to_grayscale(file):
    img_buffer = Image.open(file).convert('LA')
    img_buffer.save('greyscale.png')

# source image is 100x30
# we trim out 3 px worth border from all sides
def remove_border(file):
    img_buffer = Image.open(file)
    cropped = img_buffer.crop((3, 3, 97, 27))
    cropped.save('greyscale_cropped.png')

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
    img_buffer.save('grayscale_enhanced.png')

def strip_image(file):
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
    cropped.save('greyscale_enhanced_cropped.png')

def shear_image(file):
    img = Image.open(file)
    width, height = img.size
    m = -0.35
    xshift = abs(m) * width
    # new_width = width + int(round(xshift))
    img = img.transform((width, height), Image.AFFINE, (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
    img.save('sheared.png')

def improve_color_sheared(file):
    img_buffer = Image.open(file)
    width, height = img_buffer.size
    for x in range(0, width):
        for y in range(0, height):
            darkness = img_buffer.getpixel((x, y))[1]
            if (darkness > 160) :
                img_buffer.putpixel((x, y), (0, 255))
            else :
                img_buffer.putpixel((x, y), (0, 0))
    img_buffer.save('sheared_enhanced.png')

conver_to_grayscale(image_src)
remove_border('greyscale.png')
improve_color('greyscale_cropped.png')
strip_image('grayscale_enhanced.png')
shear_image('greyscale_enhanced_cropped.png')
improve_color_sheared('sheared.png')