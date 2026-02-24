import pygame
import numpy


class Mouse():

    def get_position(self):
        self.position = pygame.mouse.get_pos() 
        return self.position
    
    def get_state(self):
        self.state = pygame.mouse.get_pressed()
        return self.state
    
    
def get_square_under_mouse(grid: object, global_mx: int, global_my: int, board_offset: int) -> object:
    """
    Purpose:
        Convert the global position (0-1280) to the local position on the board (0-640px) when clicking the board
    Parameters:
        grid: The grid we are playing on (Object)
        mx: The global x-position of the mouse (int)
        my: The global y-position of the mouse (int)
        board_offset: How far the board is from the end of the screen
    Return Value: 
        Return the grid's chess coordinates
    """
    
    local_mx = global_mx - board_offset
    local_my = global_my  

    # 2. Check if the click is actually on the board
    if 0 <= local_mx < 640 and 0 <= local_my < 640:
        # 3. Use math to find the array indices (80 is square width)
        col = local_mx // 80
        row = local_my // 80
        
        # 4. Return the Square object from your numpy grid
        square = grid[row][col] # Get the square
        return square
        
    return None # Return None if they clicked the black sidebar
    