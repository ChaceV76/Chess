import pygame
import numpy
from board import coordinates

class Mouse():
    def __init__(self):
        self.state = pygame.mouse.get_pressed() # Get the state of the mouse if pressed or not
        self.position = pygame.mouse.get_pos() # Get the position of the mouse
        self.click = pygame.mouse.get_focused() # Check if the display is receiving mouse input

    def get_position(self):
        return self.position
    

def mouse(grid):

    mouse = Mouse()
    
    """
    Purpose: 
        Provides mouse functionality over the grid
    Parameters:
        grid: A pygame object
    Return Value:
        None, This function the mouse movement
    """
    
    # mouse_pos = pygame.mouse.get_pos()

    for row in grid: # Iterating though the rows into each specific square to access its attrubutes
        for square in row:
            if square.rect.collidepoint(mouse.get_position()):
                print("Collision with square at", square.coordinates)
                break