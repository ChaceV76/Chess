import pygame
import numpy
from board import coordinates


def mouse(grid, coordinate_system):
    """
    Purpose: 
        Provides mouse functionality over the grid
    Parameters:
        grid: A pygame object
    Return Value:
        None, This function the mouse movement
    """
    
    mouse_pos = pygame.mouse.get_pos()

    for row in grid: # Iterating though the rows into each specific square to access its attrubutes
        for square in row:
            if square.rect.collidepoint(mouse_pos):
                print("Collision with square at", coordinate_system[mouse_pos])
                break