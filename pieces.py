"""This file will be for creating class and properties for each unique piece"""
import pygame
import os.path 

base = os.path.dirname(__file__)  # Main Directory


class Pawn:
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'pawn.png')).convert_alpha(),
            (80, 80)  # match square size
        )
        self.color = color

class Bishop:
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'bishop.png')).convert_alpha(),
            (80, 80)  # match square size
        )
        self.color = color


class Knight:
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'knight.png')).convert_alpha(),
            (80, 80)  # match square size
        )
        self.color = color


class Rook:
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'rook.png')).convert_alpha(),
            (80, 80)  # match square size
        )
        self.color = color
    

class Queen(Bishop, Rook):
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
           pygame.image.load(os.path.join('images', 'Queen.png')).convert_alpha(),
           (80, 80)  # match square size
        )
        self.color = color

    

class King(Queen):
    def __init__(self, color):
        self.load_piece = pygame.transform.scale(
            pygame.image.load(os.path.join('images', 'king.png')).convert_alpha(),
            (80, 80)  # match square size
        )
        self.color = color


