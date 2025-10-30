# Max Martin - Y10CSC
import tkinter as tk

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
    cell_button = buttons[row][col]
    grid_cell = grid[row][col]

    if grid_cell == GRID_CELL_HIT:
        # already played
        ...
    elif grid_cell == GRID_CELL_MISS:
        # already played
        ...
    elif grid_cell == GRID_CELL_HAS_SHIP:
        grid_cell = GRID_CELL_HIT
        cell_button.config(text=BUTTON_CELL_HIT, state=tk.DISABLED)

    elif grid_cell == GRID_CELL_EMPTY:
        grid_cell = GRID_CELL_MISS
        cell_button.config(text=BUTTON_CELL_MISS, state=tk.DISABLED)

def setup_grid_buttons():
    # create frame to store the buttons
    board_frame = tk.Frame(root)
    # relx / rely is relative x and relative y (relative to window size)
    # 0 - 1 is from edge to edge
    # using 0.5 makes it centered
    board_frame.place(relx=0.5, rely=0.5, anchor="center")  # center the frame

    for row in range(GRID_SIZE):
        row_buttons = []
        for col in range(GRID_SIZE):
            button = tk.Button(
                board_frame,
                text=BUTTON_CELL_EMPTY,
                width=BUTTON_CELL_WIDTH,
                height=BUTTON_CELL_HEIGHT,
                command=lambda r=row, c=col: on_button_cell_clicked(r, c)
            )
            button.grid(row=row + 1, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])
            row_buttons.append(button)
        buttons.append(row_buttons)

        # add number headers (1–10)
        for col in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                text=str(col + 1),
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            label.grid(row=0, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])

        # add letter headers (A–J)
        for row in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                text=LETTERS[row],
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            label.grid(row=row + 1, column=0, padx=GRID_PADDING[0], pady=GRID_PADDING[1])


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
setup_grid_buttons()
tk.mainloop()