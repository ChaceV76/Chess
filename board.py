import pygame
import numpy as np


class Squares():
    """
    Purpose: 
        Squares Class is used to construct rectangle objects. Can set and store x and y coordinate points & manipulate colors
    Class Parameter: 
        None
    Attributes: 
        x: Screen coordinate in the horizontal plane (int/float)
        y: Screen coordinate in the vertical plane (int/float)
        Coordinates: The game coordinates (Ex:A4) (int/float)
        rect: The rectangle itself (object)
        base_color: The default color of the square (object)
        color: The current color of the square, in any state (object)
    """

    def __init__(self, x: int, y: int, row: int, column: int):
        self.x = int(x)
        self.y = int(y)
        self.coordinates = (row, column)
        self.rect = pygame.Rect((self.x, self.y), (80, 80))
        self.base_color = pygame.Color("white") # Sets our default color, "white" is just for the sake ofgetting initialized
        self.color = self.base_color # Current color whether it's default, highlited, or getting rested
        
    def set_coordinates(self, grid_coordinates): # Set the square to a chess coordinate
        self.coordinates = grid_coordinates
    
    def set_board_color(self, color): # initializes the board color
        self.base_color = pygame.Color(color) # This is where the real base color comes through
    
    def reset_color(self): # Resets back to base color
        self.color = self.base_color

    def highlight_color(self): # Highlights color when clicked and moved
        self.color = pygame.Color('Yellow')

    
def grid_construction(num_rows, num_columns, width, board_offset):
    """
    Purpose: 
        Constructs a numpy grid in 2d nested for loops
    Parameters:
        num_rows: # of Rows (int)
        num_columns: # of columns (int)
        width: size of the square (int)
    Return Value:
        It will return a 2d numpy grid (object)
    """

    grid = []

    for row in range(num_rows):
        row_data = [] # construct a empty row
        y = row * width
        for column in range(num_columns): # iterate over columns now
            x = column * width
            square = Squares(x, y, row, column) # create a squares object passing in the coordinates
            square.set_coordinates(coordinates(row, column))
            if (row + column) % 2 == 0: # Condition to create the checker pattern
                square.set_board_color('navajowhite')
            else:
                square.set_board_color('lightsalmon4')

            row_data.append(square)
    
        grid.append(row_data) # add rows to the rid
    numpy_grid = np.array(grid, dtype='object') # Convert to numpy array

            
    return numpy_grid



def draw_grid(grid, test_surface):  
    """
    Purpose: 
        Draws the 2d numpy grid onto the screen 
    Parameters:
        grid: A pygame object
        test_surface: The surface on where where we draw the grid object on
    Return Value:
        None, simply just draws the board and it's color
    """
       
    for row in grid:
        for square in row:
            pygame.draw.rect(test_surface, square.base_color, square.rect)


def coordinates(row, column):
    """
    Purpose: 
        Iterates over the grid and assigns each square a chess coordinate 
    Parameters:
        rows: # of rows (int)
        columns: # of columns (int)
    Return Value:
        A coordinate dictionary with all possible coordinates in chess notation
    """
    
    coordinate_dict = {}

    letters = "ABCDEFGH"

    char = letters[column]
    key = f"{char}{8 - row}"
    value = (row, column)

    coordinate_dict.update([(key, value)]) # Store all the coordinates into a dict   
    key = coordinate_dict.keys() # Get the key itself

    return key

    