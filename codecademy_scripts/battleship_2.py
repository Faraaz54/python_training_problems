from random import randint
from random import choice


board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

firstship_row = random_row(board)
firstship_col = random_col(board)

print firstship_row
print firstship_col

row_2 = random_row(board)
col_2 = random_col(board)

def random_row2(col1, col2, row):
    if col1 != col2:
        second_row = row
    elif col1 == col2:
        lst = [x for x in range(0, len(board) - 1) if x != row]
        second_row = choice(lst)
    return second_row

def random_col2(row1, row2, col):
    if row1 != row2:
        second_col = col
    elif row1 == row2:
        lst = [x for x in range(0, len(board) - 1) if x != col]
        second_col = choice(lst)
    return second_col

def ship_status(ship1, ship2):
    if ship1 == 1 and ship2 == 1:
        print "Congratulations, You sunk both the ships"
    elif ship1 == 0 and ship2 == 1:
        print "You failed to sink first ship, but able to sink second ship"
    elif ship1 == 1 and ship2 == 0:
        print "You sunk the first ship, but failed to sink second ship"
    elif ship1 == 0 and ship2 == 0:
        print "You failed to sink any of the ships"

secondship_row = random_row2(firstship_col, col_2, row_2)
secondship_col = random_col2(firstship_row, row_2, col_2)

print secondship_row
print secondship_col

first_ship_status = 0
second_ship_status = 0

for i in range(0,4):
    guess_row = int(raw_input("Guess First Ship Row:"))
    guess_col = int(raw_input("Guess First Ship Col:"))
    if guess_row == firstship_row and guess_col == firstship_col:
        print "Congratulations! You sank the first battleship!"
        first_ship_status = 1
        break
    elif guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
        print "You guessed it already"
    else:
        print "You missed the battleship, try again!"
    if guess_row in range(5) and guess_col in range(5):
        board[guess_row][guess_col] = "X"

print "Try sinking the second one"
print print_board(board)

for i in range(0,4):
    guess_row_2 = int(raw_input("Guess Second Ship Row:"))
    guess_col_2 = int(raw_input("Guess Second Ship Col:"))
    if guess_row_2 == secondship_row and guess_col_2 == secondship_col:
        print "Congratulations! You sank the second battleship!"
        second_ship_status = 1
        break

    elif guess_row_2 not in range(5) or guess_col_2 not in range(5):
        print "Oops, that's not even in the ocean."
    elif board[guess_row_2][guess_col_2] == "X":
        print "You guessed it already"
    else:
        print "You missed the battleship, try again!"
    if guess_row_2 in range(5) and guess_col_2 in range(5):
        board[guess_row_2][guess_col_2] = "X"


print ship_status(first_ship_status, second_ship_status )

print "Game Over"

print print_board(board)
