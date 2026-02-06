# import numpy as np

'''
grid = [] # intitilize a grid variable to append out rows to
num_rows = 8
num_columns = 8

x = 0
y = 0
for i in range(num_rows):
    row_data = [] # construct a empty row
    for column in range(num_columns): # construct column
        x += 1 # crate a variable
        row_data.append(x) # append that variable to the rowq
        

    grid.append(row_data) # append that row to the grid

    # Iteration repeats
  

board = np.array(grid)
print(board)
'''

def endsum(val):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''

    sval = str(val)
    first = sval[0]
    last = sval[len(sval)-1]

    combo = int(first) + int(last)
    return combo

if __name__ == "__main__":
    print(endsum(678))

    help(endsum)