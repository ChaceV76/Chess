import pygame
import numpy
from board import coordinates

class Mouse():
    def __init__(self):
        self.state = pygame.mouse.get_pressed() # Get the state of the mouse if pressed or not
        self.click = pygame.mouse.get_focused() # Check if the display is receiving mouse input

    def get_position(self):
        self.position = pygame.mouse.get_pos() 
        return self.position
    

def mouse(grid, board_offset):

    mouse = Mouse()
    
    """
    Purpose: 
        Provides mouse functionality over the grid
    Parameters:
        grid: A pygame object
    Return Value:
        None, This function the mouse movement
    """
    

    mx, my = mouse.get_position()
    target_square = get_square_under_mouse(grid, mx, my, board_offset)
    return target_square

def get_square_under_mouse(grid, mx, my, board_offset):
    local_mx = mx - board_offset
    local_my = my  
    
    for row in grid:
        for square in row:
            # Check if the square's rect contains the translated mouse point
            if square.rect.collidepoint(local_mx, local_my):
                return square
    return None