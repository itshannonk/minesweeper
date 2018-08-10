# Name: Shannon Komguem
# Date: January 22, 2018
# Description: Minesweeper

import random
# ROUTINES ----------------------------------
# ASSIGN MINES TO BOARD
def PlaceBom (bom, mines, row, col):
    i = 1
    while (i <= bom):
        # Generate random mine positions
        r = random.randint (0, row - 1)
        c = random.randint (0, col - 1)

        # Place mine 
        # If there's alredy a mine there generate new numbers
        if mines [r][c][1] == -1:
            # [row, col, NumMines]
            i = i - 1
        # Otherwise, place the mine
        else:
            mines [r][c][1] = -1
        i = i + 1

# COUNT MINES AROUND EACH SQUARE
def CountBom (board, row, col):
    for i in range (0, row):
        for j in range (0, col):
            # Initialize number of bombs
            bom = 0
            if board [i][j][1] != -1:
                
                # IF SQUARE IS IN FIRST ROW =========================
                if i == 0:
                    # Checks squre directly beneath it
                    if board [i + 1][j][1] == -1: bom = bom + 1
                
                    # If square is in first column
                    if j == 0:
                        # Count Squares around it
                        if board [i + 1][j + 1][1] == -1: bom = bom + 1
                        if board [i][j + 1][1] == -1: bom = bom + 1
                    # If square is in last column
                    elif j == col - 1:
                        if board [i][j - 1][1] == -1: bom = bom + 1
                        if board [i + 1][j - 1][1] == -1: bom = bom + 1
                    # If square is in the middle
                    else:
                        for x in range (i, i + 2):
                            if board [x][j - 1][1] == -1: bom = bom + 1
                            if board [x][j + 1][1] == -1: bom = bom + 1

                # IF SQUARE IS IN LAST ROW ==========================
                elif i == row - 1:
                    # Checks squre directly above it
                    if board [i - 1][j][1] == -1: bom = bom + 1
                
                    # If square is in first column
                    if j == 0:
                        # Count Squares around it
                        if board [i - 1][j + 1][1] == -1: bom = bom + 1
                        if board [i][j + 1][1] == -1: bom = bom + 1
                    # If square is in last column
                    elif j == col - 1:
                        if board [i][j - 1][1] == -1: bom = bom + 1
                        if board [i - 1][j - 1][1] == -1: bom = bom + 1
                    # If square is in the middle
                    else:
                        for x in range (i - 1, i + 1):
                            if board [x][j - 1][1] == -1: bom = bom + 1
                            if board [x][j + 1][1] == -1: bom = bom + 1

                # IF SQUARE IS IN FIRST COLUMN =======================
                elif j == 0:
                    # Check square directly to the right
                    if board [i][j + 1][1] == -1: bom = bom + 1
                    
                    # The corner squares were take care of in previous is statements
                    for x in range (j, j + 2):
                        if board [i + 1][x][1] == -1: bom = bom + 1
                        if board [i - 1][x][1] == -1: bom = bom + 1

                # IF SQUARE IS IN LAST COLUMN ========================
                elif j == col - 1:
                    # Check square directly to the left
                    if board [i][j - 1][1] == -1: bom = bom + 1
                    
                    # The corner squares were take care of in previous is statements
                    for x in range (j - 1, j + 1):
                        if board [i + 1][x][1] == -1: bom = bom + 1
                        if board [i - 1][x][1] == -1: bom = bom + 1

                # IF SQUARE IS IN THE MIDDLE =========================
                else:
                    # Check squares directly above and beneath
                    if board [i + 1][j][1] == -1: bom = bom + 1
                    if board [i - 1][j][1] == -1: bom = bom + 1

                    # Check all squares to the side
                    for x in range (i - 1, i + 2):
                            if board [x][j - 1][1] == -1: bom = bom + 1
                            if board [x][j + 1][1] == -1: bom = bom + 1

                # Assign Number to Square
                board [i][j][1] = bom
    return board

# UNCOVER BOARD      
def Uncover (board, row, col, urow, ucol):
        
    if board [urow][ucol][1] > 0:
        board [urow][ucol][0] = 1

    # If square is 0, uncover surrounding squares  
    elif board [urow][ucol][1] == 0:
        board [urow][ucol][0] = 1
        if urow != 0 and ucol != col - 1 and board [urow - 1][ucol + 1][0] == 0:
                Uncover (board, row, col, urow - 1, ucol + 1)

        if urow != row - 1 and ucol != col - 1 and board [urow + 1][ucol + 1][0] == 0:
                Uncover (board, row, col, urow + 1, ucol + 1)

        if urow != row - 1 and ucol != 0 and board [urow + 1][ucol - 1][0] == 0:
                Uncover (board, row, col, urow + 1, ucol - 1)

        if urow != 0 and ucol != 0 and board [urow - 1][ucol - 1][0] == 0:
                Uncover (board, row, col, urow - 1, ucol - 1)

        if urow != 0 and board [urow - 1][ucol][0] == 0:
                Uncover (board, row, col, urow - 1, ucol)

        if urow != row - 1 and board [urow + 1][ucol][0] == 0:
                Uncover (board, row, col, urow + 1, ucol)

        if ucol != 0 and board [urow][ucol - 1][0] == 0:
                Uncover (board, row, col, urow, ucol - 1)

        if ucol != col - 1 and board [urow ][ucol + 1][0] == 0:
                Uncover (board, row, col, urow, ucol + 1)

# DISPLAY BOARD     
def DisplayBoard (board, row, col):
    for i in range (0, col):
        print (i, end= '  ')
    print ('')
    for i in range (0, col):
        print ('---', end= '')
    print ('')
    
    n = -1
    for i in range (0, row):
        for j in range (0, col):
            if board [i][j][0] == 0:
                print ('X', end= '  ')
            elif board [i][j][0] == 1:
                print (board [i][j][1], end= '  ')
            else:
                print ('F', end= '  ')
                
        n = n + 1
        print ('| ', n)

# DISPLAY PROGRAMMER'S BOARD
def DisplayCheatBoard (board, row, col):
    for i in range (0, col):
        print (i, end= '  ')
    print ('')
    for i in range (0, col):
        print ('---', end= '')
    print ('')
    
    n = -1
    for i in range (0, row):
        for j in range (0, col):
            if board [i][j][0] == 0:
                if board [i][j][1] == -1:
                    print ('B', end= '  ')
                else:
                    print ('-', end= '  ')
            elif board [i][j][0] == 1:
                print (board [i][j][1], end= '  ')
            else:
                print ('F', end= '  ')
                
        n = n + 1
        print ('| ', n)

# CHECK UNCOVERED SQUARES
def CheckUncovered (board, row, col, bom):
    global done
    uncovered = 0
    for i in range (0, row):
        for j in range (0, col):
            if board [i][j][0] == 1:
                uncovered = uncovered + 1

    if uncovered == row * col - bom:
        done = 2
    else:
        print ('')
        print ("** You've found all the mines! Clear the board to win **")
    return done

# MAIN PROGRAM ------------------------------
# Display Instructions
print ('MINESWEEPER')
print ('1. Set board size (minimun 2x2)')
print ('2. Pick a number of mines (# of mines should be less that row x col)')
print ('3. Choose a square to flag or reveal by inputting the row and the column')
# Initialize board
row = int (input ("Enter the number of rows: "))
col = int (input ("Enter the number of columns: "))
bom = int (input ("Enter the number of bombs: "))
print ('')
board = [[[0,0] for i in range (0, row)] for i in range (0, col)]
#           ^ a list inside of the 2D list [covered, NumMines]

# Assign bombs to board
PlaceBom (bom, board, row, col)

# Count Number of Mines around spaces
CountBom (board, row, col)

done = 0
foundbom = 0
while done == 0:
    # Display Board
    DisplayBoard (board, row, col)

    # Display Programmer board
    #DisplayCheatBoard (board, row, col)
 
    option = int (input ('Enter 1 to uncover square and 2 to flag: '))
    urow = int (input ('Enter row: '))
    ucol = int (input ('Enter col: '))

    # Use User Input
    if ucol > col or urow > row: # <-- check validity
        print ('enter valid row/column')
    elif board [urow][ucol][1] == -1 and option == 1: # <-- if it's a bomb
        done = 1
    elif option == 1: # <- uncover
        Uncover (board, row, col, urow, ucol)
    elif option == 2: # <-- flag
        board [urow][ucol][0] = 2
        foundbom = foundbom + 1

    if foundbom == bom: # <-- if all the mines are flagged
        CheckUncovered (board, row, col, bom)
        
# Print exit message
if done == 1:
    print ('You hit a mine. Game Over')
else:
    print ('You won!')
    
