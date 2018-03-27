#Image resizing using Python-resize-image
from PIL import Image

def Image_resize(in_image, out_image, size):
    real_image = Image.open(in_image)
    width, height = real_image.size
    print('Size of original image {} X {}: '.format(width, height))

    resized_image = real_image.resize(size)
    width, height = resized_image.size
    print('The resized image size image {} X {}: '.format(width, height))

    resized_image.show()
    resized_image.save(out_image)

if __name__ == '__main__':
    Image_resize(in_image='real-image.jpeg', out_image='resized-image.jpeg', size=(100,100))