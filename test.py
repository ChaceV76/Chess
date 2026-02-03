import numpy as np


grid = [] # intitilize a grid variable to append out rows to
num_rows = 8
num_columns = 8

x = 0
y = 0
for i in range(num_rows):
    row_data = [] # construct a empty row
    for column in range(num_columns):
        x += 1 
        row_data.append(x)
        

    grid.append(row_data)
  
board = np.array(grid)
print(board)