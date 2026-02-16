import pygame
import numpy as np
from board import grid_construction
from board import draw_grid
from board import coordinates
from functionality import mouse
from functionality import get_square_under_mouse
import functionality


def main():
    """THIS PART SIMPLY INITIALIZES THE GAME AND RUNS THE BACKEND"""
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    running = True

    # Create the test surface
    test_surface = pygame.Surface((640, 640))
    test_surface.fill('white')
    SCREEN_OFFSET_X = 320 # How far the regular pygame surface is from the chess board surface
    chess_grid = grid_construction(8, 8, 80, SCREEN_OFFSET_X) # Creates and stores the grid object
    
    
    
    
    """THIS IS THE LOOP WHILE THE GAME RUNS. THIS IS WHAT WE SEE ON THE SCREEN"""
    while running:
        for event in pygame.event.get():
            draw_grid(chess_grid, test_surface) # Draws the grid

            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos # Retitns the live mouse location like a tule (x, y) then unpack it
                clicked_square = get_square_under_mouse(chess_grid, mx, my, SCREEN_OFFSET_X)
        
                if clicked_square:
                # Now we can interact with the square object!
                    print(f"Clicked: {clicked_square.coordinates}")
                    clicked_square.highlight_color() 
                    """CREATE A HiGHLIGHT COMMAND"""

        
        screen.fill('black')

        # RENDER GAME HERE USING BLIT
        screen.blit(test_surface, (SCREEN_OFFSET_X, 0))
        

        # flip() the display to put work on screen
        pygame.display.flip()

        clock.tick(60) # Limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()