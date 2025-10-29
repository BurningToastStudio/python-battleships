# Max Martin - Y10CSC

# grid will be stored as 2d array
grid = []
grid_size = 10


CELL_EMPTY = ""
CELL_HAS_SHIP = "o"

CELL_HIT = "x"
CELL_MISS = "."


def setup_grid():
    # create 2d array
    for i in range(grid_size):
        row = [] # create a row
        for j in range(grid_size):
            row.append(CELL_EMPTY) # put empty cells into that row
        grid.append(row) # add the row with empty cells to the grid
        # loop again with a new row


setup_grid()
for row in grid:
    print(row)




