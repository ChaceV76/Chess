import pygame
import numpy as np
import pieces
import sys

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
        self.base_color = pygame.Color("white") # Sets our default color, "white" is just for the sake of getting initialized
        self.color = self.base_color # Current color whether it's default, highlighted, or getting reseted
        self.highlighted = False
        self.piece = None 
        
        
    def set_coordinates(self, grid_coordinates: dict) -> None: # Set the square to a chess coordinate
        self.coordinates = grid_coordinates
    
    def set_board_color(self, color: str) -> None: # initializes the board color
        self.base_color = pygame.Color(color) # This is where the real base color comes through
    
    def reset_color(self) -> None: # Resets back to base color
        self.color = self.base_color

    def set_piece(self, specific_piece: object) -> None: 
        self.piece = specific_piece

    
def grid_construction(num_rows: int, num_columns: int, width: int) -> object:
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

    # Layout for the starting pieces in back row
    back_row = [pieces.Rook, pieces.Knight, pieces.Bishop, pieces.Queen, pieces.King, pieces.Bishop, pieces.Knight, pieces.Rook]

    for row in range(num_rows):
        row_data = [] # construct a empty row
        y = row * width
        for column in range(num_columns): # iterate over columns now
            x = column * width
            square = Squares(x, y, row, column) # create a squares object passing in the coordinates
            square.set_coordinates(coordinates(row, column)) 

            '''Condition to create the checker pattern'''
            if (row + column) % 2 == 0: 
                square.set_board_color('navajowhite')
            else:
                square.set_board_color('lightsalmon4')
            
            '''This condition will be used to check if pieces should be generated on the row'''
            if row in [0, 1, 6, 7]:
                if row == 0 or row == 7: # if its in the first and last row
                    if row == 0: # if it's the top back row assign the pieces color to black
                        square.set_piece(back_row[column]("black"))
                    else:
                        square.set_piece(back_row[column]("white")) # set it color to white
                else:
                    if row == 1:
                        square.set_piece(pieces.Pawn("black"))
                    else:
                        square.set_piece(pieces.Pawn("white"))
                
            row_data.append(square)
    
        grid.append(row_data) # add rows to the rid

    numpy_grid = np.array(grid, dtype='object') # Convert to numpy array
    return numpy_grid


def draw_grid(grid: object, test_surface: object) -> None:  
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

            if square.highlighted:
                print(f"Highlighting {square.coordinates}")
                test_surface.fill((255, 255, 0), square.rect)
                

             # draw the piece on top if one exists
            if square.piece is not None:
                piece_surface = square.piece.load_piece
                test_surface.blit(piece_surface, square.rect)
            

def coordinates(row : int, column: int) -> dict:
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

    try:
        letters = "ABCDEFGH"

        char = letters[column]
        key = f"{char}{8 - row}"
        value = (row, column)

        coordinate_dict.update([(key, value)]) # Store all the coordinates into a dict  
        return key
    
    except KeyError:
        raise SystemExit('Key does not exist')

    