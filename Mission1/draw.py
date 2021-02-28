"""Gannon Leech, November 17, 2019
This file contains code for the draw code function, which generates an image
based off of a list of code that is inputted. This can either be binary code, 
gray code, or anti gray code, and then generates an image of squares with 
different colors depending on if the corresponding bit is a 1 or a 0"""

from PIL import Image, ImageDraw
from image import create_image, draw_square, save_image
from convert import binary_code, gray_code, anti_gray_code
import sys

# Determines Image Dimensions
SWATCH_WIDTH = 32
IMAGE_OFFSET = 3
SWATCH_OFFSET = 2

# Colors
ZERO_COLOR = (100, 100, 100)
ONE_COLOR = (255, 87, 51)


def draw_code(filename, code, n):
    """
    Generates an image that represents a sequence of encoded integers.
    'code' is a list containing 2**n elements.
    Each element of 'code' is a list of 'n' bits
    This image represents 'code' by coloring square swatches to represent
    the digits of each element in the sequence.
    """
    width = n * SWATCH_WIDTH
    height = 2 ** n * SWATCH_WIDTH
    my_image = create_image(width - IMAGE_OFFSET, height - IMAGE_OFFSET)
    
    for row, element in enumerate(code):
        for column, bit in enumerate(element):
            #iterates through each element in the rows and columns of the list
            #and draws the squares in the corresponding colors
            if bit == 0:
                draw_square(my_image, column * SWATCH_WIDTH - SWATCH_OFFSET, \
                            row * SWATCH_WIDTH, SWATCH_WIDTH - SWATCH_OFFSET,\
                            ZERO_COLOR)
            else:
                draw_square(my_image, column * SWATCH_WIDTH - SWATCH_OFFSET,\
                            row * SWATCH_WIDTH, SWATCH_WIDTH - SWATCH_OFFSET,\
                            ONE_COLOR)
                
    save_image(my_image, filename)
            
    

if __name__ == '__main__':
    n = int(sys.argv[1])
    code = gray_code(n)
    draw_code("gray.png", code, n)
    code = anti_gray_code(n)
    draw_code("antigray.png", code, n)
    code = binary_code(n)
    draw_code("binary.png", code, n)
