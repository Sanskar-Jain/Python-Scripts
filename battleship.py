# Python Script for Battleship Project.


# Imports randint function form random library to generate random variables.
from random import randint

# Empty list
board = []

# Empty list initialised containing 5 lists representing a 2-D Matrix.
for x in range(5):
    board.append(["O"] * 5)

# Function to print the values of 2-D Matrix.
def print_board(board):
    for row in board:
        print(" ".join(row))

# Calling function print_board to print the board on console in form of 2-D Matrix.
print("Let's play Battleship!")
print_board(board)

# Function to set the row no. of battleship randomly using randint.
def random_row(board):
    return randint(0, len(board) - 1)

# Function to set the col no. of battleship randomly using randint.
def random_col(board):
    return randint(0, len(board[0]) - 1)

# Assigning the randomly chosen row and col values of battleship to ship_row and ship_col.
ship_row = random_row(board)
ship_col = random_col(board)

# Printing the Exact location of BattleShip.
print(ship_row)
print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
# Aceepts user input 4 times for position of BattleShip and responds accordingly.
for j in range(4):

    # Prints the loop control variable.
    print("Turn ",j + 1)

    # Asks user for input.
    guess_row = int(input("Guess Row : "))
    guess_col = int(input("Guess Col : "))

    # Checks if position entered is same as position of BattleShip and breaks the loop if user wins.
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship.")
        break

    # Checks for another possibilities.
    else:
        # Checks if user hasn't supplied any out of range row and column values
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")

        # Checks if user hasn't selected any value twice.
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")

        # Checks if user Looses.
        else:
            print("You missed my battleship!!")
            board[guess_row][guess_col] = "X"
        print_board(board)
        if j == 3:
            print("Game Over!")
        j += 1