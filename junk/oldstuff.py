def create_empty_board(size):
    # Creates an empty square shaped board with a side length of 'size'
    board = []
    for y in range(0,size):
        row = [] 
        for x in range(0,size):
            row.append("_")
        board.append(row)
    return board


def print_board(board,size):
    # prints the board and the numbers around it
    print()

    # x-axis numbers on top of the board
    print("  ",end="")
    for n in range(0,size):
        print(n,end=" ")
    print()

    # board and y-axis numbers (row_number)
    for row_number in range(0,size):
        print(row_number,end=" ")
        for char in board[row_number]:
            print(char,end=" ")
        print()

    print()


def ask_coordinates():
    # asks coordinates from user (x-y)
    cord = input("x-y: ")
    x = int(cord[0])
    y = int(cord[-1])
    return (x,y)


def put_in_board(char,x,y,board):
    # puts 'char' to coordinates 'x,y' in 'board'
    board[x][y] = char


def count_upwards(x,y,board,mark):
    matches = 0
    cursorX = x
    cursorY = y - 1
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorY == 0: # reached top end of board
            break

        cursorY -= 1
        cursor = board.squares[cursorX,cursorY]

    return matches


def count_downwards(x,y,board,mark):
    matches = 0
    cursorX = x
    cursorY = y + 1
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorY == board.height - 1: # reached bottom of board
            break

        cursorY += 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches


def check_vertical(x,y,board):
    # Check vertical lines and count matches
    mark = board.squares[x,y]
    matches = 0

    if y > 0:
        matches += count_upwards(x,y,board,mark)
    if y < board.height -1:
        matches += count_downwards(x,y,board,mark)

    return matches


def count_right(x,y,board,mark):
    # Count matches starting from x,y and moving towards right
    # Counting stops when different mark is noticed
    matches = 0
    cursorX = x + 1 
    cursorY = y 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == board.width - 1: # reached right side of board
            break

        cursorX += 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches


def count_left(x,y,board,mark):
    # Count matches starting from x,y and moving towards left
    # Counting stops when different mark is noticed
    matches = 0
    cursorX = x - 1 
    cursorY = y 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == 0: # reached right side of board
            break

        cursorX -= 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches


def check_horizontal(x,y,board):
    # Check horizontal lines and count matches
    mark = board.squares[x,y]
    matches = 0

    if x < board.width -1:
        matches += count_right(x,y,board,mark)
    if x > 0:
        matches += count_left(x,y,board,mark)
    
    return matches


def count_upright(x,y,board,mark):
    # Count matches starting from x,y and moving towards north west
    # Counting stops when different mark is noticed
    matches = 0
    cursorX = x + 1 
    cursorY = y - 1 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == board.height-1  or cursorY == 0: 
            break

        cursorX += 1
        cursorY -= 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches


def count_downleft(x,y,board,mark):
    # Count matches starting from x,y and moving towards south east.
    # Counting stops when different mark is noticed
    matches = 0
    cursorX = x - 1 
    cursorY = y + 1 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == 0 or cursorY == board.height - 1: 
            break

        cursorX -= 1
        cursorY += 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches

    
def check_diagonal1(x,y,board):
    # Checks diagonal lines (from up right to down left)
    mark = board.squares[x,y]
    matches = 0

    if x < board.width - 1 and y > 0:
        matches += count_upright(x,y,board,mark)
    if x > 0 and y > board.height - 1:
        matches += count_downleft(x,y,board,mark)
    
    return matches


def count_upleft(x,y,board,mark):
    matches = 0
    cursorX = x - 1 
    cursorY = y - 1 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == 0 or cursorY == 0: 
            break

        cursorX -= 1
        cursorY -= 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches
    

def count_downright(x,y,board,mark):
    matches = 0
    cursorX = x + 1 
    cursorY = y + 1 
    cursor = board.squares[cursorX,cursorY]

    while cursor == mark:
        matches += 1

        if cursorX == board.width - 1 or cursorY == board.height - 1: 
            break

        cursorX += 1
        cursorY += 1
        cursor = board.squares[cursorX,cursorY]
    
    return matches

def check_diagonal2(x,y,board):
    # Checks diagonal lines (from up left to down right)
    mark = board.squares[x,y]
    matches = 0

    if x > 0 and y > 0:
        matches += count_upleft(x,y,board,mark)
    if x < board.width - 1 and y < board.height - 1:
        matches += count_downright(x,y,board,mark)
    
    return matches

def check_victory(board,x,y,needed):
    # Checks if there's a winning line in 'board'.
    # Checking starts from the coordinates of the latest move ('x','y').
    # Winning line must have lenght of 'needed'.

    if check_vertical(x,y,board) >= needed - 1:
        return True
    if check_horizontal(x,y,board) >= needed - 1:
        return True
    if check_diagonal1(x,y,board) >= needed - 1:
        return True
    if check_diagonal2(x,y,board) >= needed -1:
        return True

