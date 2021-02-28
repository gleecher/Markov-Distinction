"""
Learning Objectives
- Let's remember Python!
- What would a Markov chain look like in code?

Example of an Markov Chain implementation in Python (using concepts we learned
in 1101).

Dependencies: numpy, scipy
"""

import numpy as np
import math
import random
from PIL import Image, ImageDraw


class MarkovArtist:
    def __init__(self, transition_matrix):
        """Simulates an artisht that relies on a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
                num_squares (int): the number of squares in a row
                num_rows (int): the number of rows
        """
        self.transition_matrix = transition_matrix
        self.redval = random.randint(0, 255)
        self.greenval = random.randint(0, 255)
        self.blueval = random.randint(0, 255)

    def calc_new_red(self):
        """Simulates an artisht that relies on a simple Markov chain.
        """        
        self.redval = np.random.choice(range(0,255), p = self.transition_matrix[self.redval])
        
    def calc_new_green(self):
        """Simulates an artisht that relies on a simple Markov chain.
        """          
        self.greenval = np.random.choice(range(0,255), p = self.transition_matrix[self.greenval])
        
    def calc_new_blue(self):
        """Simulates an artisht that relies on a simple Markov chain.
        """          
        self.blueval = np.random.choice(range(0,255), p = self.transition_matrix[self.blueval])


    def draw_image(self):
        """Simulates an artisht that relies on a simple Markov chain.
        """          
        w = 500
        h = 500
        
        img = Image.new("RGB", (w, h)) 
        
        for i in range(10, h - 10, 10): 

            for j in range(10, w - 10, 10):
                self.calc_new_red()
                self.calc_new_green()
                self.calc_new_blue()
                
                color = (self.redval, self.greenval, self.blueval)
                
                shape = [(i, j), ( i + 10, j + 10)] 
                img1 = ImageDraw.Draw(img)   
                img1.rectangle(shape, fill = color)            
 
        img.show() 
        
    

def main():
    transition_matrix = make_transition_matrix()
    art_maker = MarkovArtist(transition_matrix)
    art_maker.draw_image()
   

def make_transition_matrix():
    """Simulates an artisht that relies on a simple Markov chain.
    """      
    transition_matrix = []

    for i in range(255):
        sum_val= 0
        transition_matrix.append([])
        for j in range(255):
            transition_matrix[i].append(abs(i - j))
            transition_matrix[i][j] = math.pow(transition_matrix[i][j], 4)
            sum_val = sum_val + transition_matrix[i][j]
        for j in range(255):
            transition_matrix[i][j] = float(transition_matrix[i][j] / sum_val)            
                   
    return transition_matrix


if __name__ == "__main__":
    main()
