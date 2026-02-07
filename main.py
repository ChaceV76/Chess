import pygame
import numpy as np
from board import grid_construction
from board import draw_grid
from board import coordinates
from functionality import mouse


def main():
    """THIS PART SIMPLY INITIALIZES THE GAME AND RUNS THE BACKEND"""
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    running = True

    # Create the test surface
    test_surface = pygame.Surface((640, 640))
    test_surface.fill('white')

    chess_grid = grid_construction(8, 8, 80) # Stores the grid object

    chess_coordinates = coordinates(chess_grid)
    
    draw_grid(chess_grid, test_surface) # Draw the grid
    
    
    """THIS IS THE LOOP WHILE THE GAME RUNS. THIS IS WHAT WE SEE ON THE SCREEN"""
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')

        # RENDER GAME HERE USING BLIT
        screen.blit(test_surface, (320, 0))

        mouse(chess_grid, chess_coordinates) # Using the mouse

        # flip() the display to put work on screen
        pygame.display.flip()

        clock.tick(60) # Limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()