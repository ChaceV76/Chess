'''This file will be used to generate the board and pieces visually'''
import pygame
import numpy as np

class Squares():
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect((self.x, self.y), (80, 80))
        self.base_color = pygame.Color("navajowhite")
    
    def set_color(self, color):
        self.base_color = pygame.Color(color)
    
    def reset_color(): # Resets color
        pass

    def highlight_color(): # Highlights color when clicked and moved
        pass

# Sets up pygaame "Turning on Engine"
pygame.init()
screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
running = True

# Create the test surface
test_surface = pygame.Surface((640, 640))
test_surface.fill('white')

    
grid = [] # intitilize a grid variable to append rows to
num_rows = 8
num_columns = 8

for row in range(num_rows):
    row_data = [] # construct a empty row
    y = row * 80 
    for column in range(num_columns): # iterate over columns now
        x = column * 80
        square = Squares(x, y) # create a squares object passing in the coordinates
        if (row + column) % 2 == 0: # Condition to create the checker pattern
            square.set_color('navajowhite')
        else:
            square.set_color('lightsalmon4')

        row_data.append(square)
    
    grid.append(row_data)
    chess_board = np.array(grid, dtype='object')



while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    # RENDER GAME HERE USING BLIT
    screen.blit(test_surface, (320, 0))

    # flip() the display to put work on screen
    pygame.display.flip()

    clock.tick(60) # Limits FPS to 60

pygame.quit()
