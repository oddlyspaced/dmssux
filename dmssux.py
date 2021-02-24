from PIL import Image

image_src = '/home/hardik/Projects/Python-Stuff/dmssux/original/12.png'

def conver_to_grayscale(file):
    img_buffer = Image.open(file).convert('LA')
    img_buffer.save('greyscale.png')

conver_to_grayscale(image_src)