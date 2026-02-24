"""This file will be for creating class and properties for each unique piece"""
import pygame

class Pawn:
    def __init__(self, x: int, y: int):
        self.piece = pygame.image.load('images/pawn.png').convert_alpha()
        self.surface = self.piece # create a surface that matches with out image size
        self.resized_piece = pygame.transform.scale(self.surface, (16, 16)) 
        self.rect = self.surface.get_rect() # Create a rect out of our surface for collision
        self.rect.topleft = (x, y)  # Position it


class Bishop:
    pass

class Knight:
    pass

class Rook:
    pass

class Queen(Bishop, Rook):
    pass

class King(Queen):
    pass

'''
Create two classes for teams inherting all the pieces
class White(Pawn, Bishop, Knight, Rook, Queen, King):
    pass

class Black(Pawn, Bishop, Knight, Rook, Queen, King):
    pass
'''