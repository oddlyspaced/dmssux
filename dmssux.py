from PIL import Image

image_src = '/home/hardik/Projects/Python-Stuff/dmssux/original/12.png'

def conver_to_grayscale(file):
    img_buffer = Image.open(file).convert('LA')
    img_buffer.save('greyscale.png')

# source image is 100x30
# we trim out 3 px worth border from all sides
def remove_border(file):
    img_buffer = Image.open(file)
    cropped = img_buffer.crop((3, 3, 97, 27))
    cropped.save('greyscale_cropped.png')

conver_to_grayscale(image_src)
remove_border('greyscale.png')