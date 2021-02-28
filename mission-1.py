"""
Gannon Leech
02.28.21
CSCI 3725 - Computational Creativity
Mission 3: A Markov Distinction

Description: When run, this file creates and displayed piece of artwork using 
a markov chain. The image should look like a bunch of little squares in a row, 
where each color should be different, but consecutive squares in a row should 
have on average similar colors, although this affect can be adjusted based on
the powers used when creating the tranisition matrix.

No Known Bugs
"""

import numpy as np
import math
import random
from PIL import Image, ImageDraw


class MarkovArtist:
    def __init__(self, transition_matrix):
        """Simulates an artisht that relies on a  Markov chain.
           Args:
                transition_matrix (list): transition probabilities

        """
        self.transition_matrix = transition_matrix
        
        #initializes the red, blue, and green values randomly
        self.redval = random.randint(0, 255)
        self.greenval = random.randint(0, 255)
        self.blueval = random.randint(0, 255)

    def calc_new_red(self):
        """
        Decides what the next value for red should be based on the current val
        """        
        self.redval = np.random.choice(range(0,255), p = self.transition_matrix[self.redval])
        
    def calc_new_green(self):
        """
        Decides what the next value for green should be based on the current val
        """          
        self.greenval = np.random.choice(range(0,255), p = self.transition_matrix[self.greenval])
        
    def calc_new_blue(self):
        """
        Decides what the next value for blue should be based on the current val
        """          
        self.blueval = np.random.choice(range(0,255), p = self.transition_matrix[self.blueval])


    def draw_image(self, width, height, offset):
        """
        Draws and displays the image of rows of squares filled by colors 
        selected through a markov process
        """          

        img = Image.new("RGB", (width, height)) 
        
        for i in range(offset, height - offset, offset): 

            for j in range(offset, width - offset, offset):
                self.calc_new_red()
                self.calc_new_green()
                self.calc_new_blue()
                
                color = (self.redval, self.greenval, self.blueval)
                
                shape = [(i, j), ( i + offset, j + offset)] 
                img1 = ImageDraw.Draw(img)   
                img1.rectangle(shape, fill = color)            
 
        img.show() 
        
    

def main():
    val = int(input("Please enter an integer value for how much randomness \
will be in the system (1 = very random, 5 and above = less random): "))
    transition_matrix = make_transition_matrix(val)
    art_maker = MarkovArtist(transition_matrix)
    art_maker.draw_image(500, 500, 10)
   

def make_transition_matrix(power):
    """
    Creates a 255 x 255 matrix where each value is the probability of going from
    the the index of row to the index of the column
    
         power (int): the power to which the difference between the current val
         and the next val will be raised to
    """      
    transition_matrix = []

    for i in range(255):
        sum_val= 0
        transition_matrix.append([])
        for j in range(255):    
            #Fills in the matrix so that the weight is highest for a value to
            #become a nearby value. This affect can be increased by choosing a
            #larger power on line 96, examples of differnt powers are included
            
            transition_matrix[i].append(abs(i - j))
            transition_matrix[i][j] = math.pow(transition_matrix[i][j], power)
            sum_val = sum_val + transition_matrix[i][j]
            
        for j in range(255):
            #Normalizes each index of the matrix so that it is a probability and 
            #the sum of every row is 1.0
            
            transition_matrix[i][j] = float(transition_matrix[i][j] / sum_val)                 
    return transition_matrix


if __name__ == "__main__":
    main()
