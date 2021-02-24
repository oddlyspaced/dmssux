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
                img_buffer.putpixel((x, y), (255, 255))
    img_buffer.save('grayscale_enhanced.png')

conver_to_grayscale(image_src)
remove_border('greyscale.png')
improve_color('greyscale_cropped.png')