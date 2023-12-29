"""
File: fire.py
Name:Austin Chen
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
 
    gray_img = SimpleImage('photoshop_practice/images/greenland-fire.png')
    for pixel in gray_img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return gray_img


def main():
   
    original_fire = SimpleImage('photoshop_practice/images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('photoshop_practice/images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
