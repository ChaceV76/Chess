'''This file will be used to generate the board and pieces visually'''
import pygame
import numpy as np

# Sets up pygaame "Turning on Engine"
pygame.init()
screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
running = True


# Create the test surface
test_surface = pygame.Surface((640, 640))
test_surface.fill('lightsalmon4')


# Make a class for these squares and get their coordinates
class Squares():
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect((self.x, self.y), (80, 80))

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
# Create a 2D Numpy array to give us rows and columns
chess_board = np.array([])
    
num_objects = 64

# This loop will create a new row with the square objects
for i in range(num_objects):
    new_square = Squares(0, 0)
    chess_board.vstack(new_square)

pygame.draw.rect(test_surface, 'navajowhite', A8.rect)




'''
# Make a loop that skips over to the right by 80 width and fills a 80x80 navajo white rectangle after each 4th iteration move down a line
for index, _ in enumerate(range(63)):
    x = square.copy()
    x.move(80, 0)
    pygame.draw.rect(test_surface, 'navajowhite', x)
'''

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
