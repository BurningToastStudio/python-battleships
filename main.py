# Max Martin - Y10CSC

#region Imports
import tkinter as tk
import random

#endregion

#region Window setup
root = tk.Tk()
root.geometry("470x470")
root.title("Battleships")
root.resizable(False, False)
#endregion

#region Globals
# grid will be stored as 2d array
grid = []
buttons = []  # 2D list array to store all button references
ship_cells_guessed = 0 # keep track of how many ships cells have been hit
total_ship_cells = 0
guess_count = 0
#endregion

#region Constants
GRID_SIZE = 10
# TODO: support larger grid sizes
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# how the cell states are stored in the grid
GRID_CELL_EMPTY = " "
GRID_CELL_HAS_SHIP = "o"
GRID_CELL_HIT = "x"
GRID_CELL_MISS = "."

# how the cell states are stored visually on the buttons
BUTTON_CELL_EMPTY = " "
#BUTTON_CELL_HAS_SHIP = "o"
BUTTON_CELL_HIT = "X"
BUTTON_CELL_MISS = "O"

BUTTON_CELL_FONT = "Arial", 50
BUTTON_CELL_WIDTH = 4
BUTTON_CELL_HEIGHT = 2

LABEL_CELL_FONT = "Arial", 10, "bold"
LABEL_CELL_WIDTH = 4
LABEL_CELL_HEIGHT = 2

OCEAN_CELL_COLOR = "navyblue"
HIT_CELL_COLOR = "red"
MISS_CELL_COLOR = "grey"

GRID_PADDING = (0, 0)
#endregion

#region Main Logic
def setup_grid():
    # create 2d array
    for i in range(GRID_SIZE):
        row = []  # create a row
        for j in range(GRID_SIZE):
            row.append(GRID_CELL_EMPTY)  # put empty cells into that row
        grid.append(row)  # add the row with empty cells to the grid

def on_button_cell_clicked(row, col):
    global ship_cells_guessed, guess_count
    guess_count += 1 # increment total guesses

    # check if the grid cell has a ship or not
    if grid[row][col] == GRID_CELL_HAS_SHIP: # that cell has a ship
        ship_cells_guessed += 1 # increment correct guesses
        grid[row][col] = GRID_CELL_HIT
        # change it to hit
        buttons[row][col].config(text=BUTTON_CELL_HIT, state=tk.DISABLED, bg=HIT_CELL_COLOR)

    elif grid[row][col] == GRID_CELL_EMPTY: # that cell is empty
        grid[row][col] = GRID_CELL_MISS
        # change it to miss
        buttons[row][col].config(text=BUTTON_CELL_MISS, state=tk.DISABLED, bg=MISS_CELL_COLOR)

    win_check() # after every guess, check if player has won

def win_check():
    if ship_cells_guessed == total_ship_cells:
        has_won()

def has_won():
    root.destroy() # close window
    i = 0
    # prints you have won a bunch of times
    while i < 50: # TODO: add a way to restart & dont use the terminal
        print(f"YOU HAVE WON IN {guess_count} GUESSES")
        i += 1 # basic itterator


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
                bg=OCEAN_CELL_COLOR,
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
    global total_ship_cells
    total_ship_cells = 17 # TODO: make this automaticly change
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

#endregion

#region DEBUGGING FUNCTION
def print_grid():
    for row in grid:
        print(row)
#endregion

setup_grid()
place_ships()
setup_grid_buttons()
tk.mainloop()