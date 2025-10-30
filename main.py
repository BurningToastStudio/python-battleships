# Max Martin - Y10CSC
import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x500")
root.title("Battleships")
#root.resizable(False, False)


# grid will be stored as 2d array
grid = []
buttons = []  # 2D list array to store all button references

GRID_SIZE = 10
# TODO: support larger grid sizes
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# how the cell states are stored in the grid
GRID_CELL_EMPTY = ""
GRID_CELL_HAS_SHIP = "o"
GRID_CELL_HIT = "x"
GRID_CELL_MISS = "."

# how the cell states are stored visually on the buttons
BUTTON_CELL_EMPTY = ""
#BUTTON_CELL_HAS_SHIP = "o"
BUTTON_CELL_HIT = "X"
BUTTON_CELL_MISS = "O"

BUTTON_CELL_FONT = "Arial", 50
BUTTON_CELL_WIDTH = 4
BUTTON_CELL_HEIGHT = 2

LABEL_CELL_FONT = "Arial", 10, "bold"
LABEL_CELL_WIDTH = 4
LABEL_CELL_HEIGHT = 2

GRID_PADDING = (0, 0)


def setup_grid():
    # create 2d array
    for i in range(GRID_SIZE):
        row = []  # create a row
        for j in range(GRID_SIZE):
            row.append(GRID_CELL_EMPTY)  # put empty cells into that row
        grid.append(row)  # add the row with empty cells to the grid

def on_button_cell_clicked(row, col):

    # check if the grid cell has a ship or not
    if grid[row][col] == GRID_CELL_HAS_SHIP:
        grid[row][col] = GRID_CELL_HIT
        # change it to hit
        buttons[row][col].config(text=BUTTON_CELL_HIT, state=tk.DISABLED)

    elif grid[row][col] == GRID_CELL_EMPTY:
        grid[row][col] = GRID_CELL_MISS
        # change it to miss
        buttons[row][col].config(text=BUTTON_CELL_MISS, state=tk.DISABLED)

def setup_grid_buttons():
    # create frame to store the buttons
    board_frame = tk.Frame(root)
    # relx / rely is relative x and relative y (relative to window size)
    # 0 - 1 is from edge to edge
    # using 0.5 makes it centered
    board_frame.place(relx=0.5, rely=0.5, anchor="center")  # center the frame

    for row in range(GRID_SIZE): # loop for every row in grid
        row_buttons = [] # store that rows buttons
        for col in range(GRID_SIZE): # for every coll in that row
            button = tk.Button( # create button
                board_frame,
                text=BUTTON_CELL_EMPTY,
                width=BUTTON_CELL_WIDTH,
                height=BUTTON_CELL_HEIGHT,
                command=lambda r=row, c=col: on_button_cell_clicked(r, c) # will call this when clicked
            )
            # place on grid
            # extra row and col because then it wont overlap with the letter and number headers
            button.grid(row=row + 1, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])
            row_buttons.append(button) # add the row to the list
        buttons.append(row_buttons) # put the finished row in the list

        # add number headers (1–10)
        for col in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                text=str(col + 1),
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            # add number to every col
            # +1 to stop overlap
            # get the grid padding tuple
            label.grid(row=0, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])

        # add letter headers (A–J)
        for row in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                # get the letter that corresponds with the row number
                text=LETTERS[row],
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            # same as above but for rows
            label.grid(row=row + 1, column=0, padx=GRID_PADDING[0], pady=GRID_PADDING[1])

def place_ships():
    # save ship type and size to a dictionary
    ships = {
        "Carrier": 5,
        "Battleship": 4,
        "Destroyer": 3,
        "Submarine": 3,
        "Patrol Boat": 2
    }

    # go through all ships
    for name, size in ships.items():
        print(f"Placing: {name}, {size}") # the print statements are for debugging purposes
        placed = False
        while not placed: # will keep trying until a valid placement is found
            # when a ship is placed in a valid position, it will return true
            placed = try_place_ship(name, size)

    print_grid()


def try_place_ship(name, size):
    # pick a random row and col
    # -1 because index starts at 0
    row = random.randint(0, GRID_SIZE - 1)
    col = random.randint(0, GRID_SIZE - 1)
    # pick random direction
    directions = ["up", "down", "left", "right"]
    direction = random.choice(directions)

    # where the coord of each ship segment will be stored
    # do this to verify its valid later
    coords = []
    for i in range(size):  # iterate over each segment of the current ship
        r, c = row, col  # start from the initial position of the ship
        # move the row or column for the rotation and what segment we are placing
        # i var is the index of the ship segment (the first one is 0)
        if direction == "up":
            r -= i
        elif direction == "down":
            r += i
        elif direction == "left":
            c -= i
        elif direction == "right":
            c += i

        # store the coordinate for this segment
        coords.append((r, c))

    # check the ship cells are within the grid
    # any() goes through every cell coord of the ship (will return bool)
    # the for loop at the end tells the any() function to loop through all elements individually
    # the row or col must not be less than 0 or greater than grid size
    if any(r < 0 or r >= GRID_SIZE or c < 0 or c >= GRID_SIZE for r, c in coords):
        print(f"Segment placement failed ({r}, {c} out of bounds), trying again")
        return False

    # check overlap
    if any(grid[r][c] == GRID_CELL_HAS_SHIP for r, c in coords):
        print(f"Segment placement failed ({r}, {c} overlap), trying again")
        return False

    # place ship on grid
    for r, c in coords:
        print(f"{name} segment placed: {r}, {c}")
        grid[r][c] = GRID_CELL_HAS_SHIP
    print(f"Placing {name} complete\n")

    return True


#region DEBUGGING FUNCTIONS
def guess_all_cells():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            on_button_cell_clicked(row, col)

def print_grid():
    for row in grid:
        print(row)
#endregion

setup_grid()
place_ships()
setup_grid_buttons()
guess_all_cells()
tk.mainloop()