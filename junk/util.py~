def ask_coordinates(board):
    # asks coordinates from user 
    while True:
        cord = input("x-y: ")
        x = int(cord[0])
        y = int(cord[-1])
        if (x,y) not in board.empty_slots:
            print("Not free!")
        else:
            return (x,y)


def check_victory(board,x,y,needed):
    # Checks if there is a winning line in 'board'
    if board.squares[(x,y)] == "X":
        coordinates = board.x_coordinates
    elif board.squares[(x,y)] == "O":
        coordinates = board.o_coordinates

    if count_vertical(coordinates,x,y) >= needed:
        return True
    elif count_horizontal(coordinates,x,y) >= needed:
        return True
    elif count_diagonal1(coordinates,x,y) >= needed:
        return True
    elif count_diagonal2(coordinates,x,y) >= needed:
        return True
    else:
        return False


def check_tie(board):
    # Checks if there's a tie
    return len(board.empty_slots) == 0

def count_upwards(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        y -= 1

    return matches


def count_downwards(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        y += 1

    return matches


def count_vertical(coordinates,x,y):
    matches = 1 # the one that was just put
    matches += count_upwards(coordinates,x,y-1)
    matches += count_downwards(coordinates,x,y+1)
    return matches 


def count_right(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x += 1

    return matches
    

def count_left(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x -= 1

    return matches


def count_horizontal(coordinates,x,y):
    matches = 1 # the one that was just put
    matches += count_right(coordinates,x+1,y)
    matches += count_left(coordinates,x-1,y)
    return matches 


def count_upright(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x += 1
        y -= 1

    return matches


def count_downleft(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x -= 1
        y += 1

    return matches


def count_diagonal1(coordinates,x,y):
    # from up right to down left
    matches = 1 # the one that was just put
    matches += count_upright(coordinates,x+1,y-1)
    matches += count_downleft(coordinates,x-1,y+1)
    return matches 


def count_upleft(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x -= 1
        y -= 1

    return matches


def count_downright(coordinates,x,y):
    matches = 0
    while (x,y) in coordinates:
        matches += 1
        x += 1
        y += 1

    return matches


def count_diagonal2(coordinates,x,y):
    # from up left to down right
    matches = 1 # the one that was just put
    matches += count_upleft(coordinates,x-1,y-1)
    matches += count_downright(coordinates,x+1,y+1)
    return matches 


