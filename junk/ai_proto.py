
def strategies(board,needed):
    height = board.height
    width = board.width

    # Vertical lines. Base moves down
    vlines = []
    for i in range(needed):
        y = usrY+i
        line = []
        for j in range(needed):
            if (usrX,y) not in board.empty_slots:
                del line
                break
            line.append((usrX,y-j))
        if (usrX,usrY) in line:
            line.remove((usrX,usrY))
        vlines.append(line)


    # Horizontal lines. Base moves left.
    hlines = []
    for i in range(needed):
        x2 = x-i
        if x2 < 0 or (x2+needed-1) > width-1: # would go over the board
            continue
        line = []
        for j in range(needed):
            line.append((x2+j,y))
        if (x,y) in line:
            line.remove((x,y))
        hlines.append(line)


    # Diagonal lines, upleft to downright. Base moves downright.
    d1lines = []
    for i in range(needed):
        x2 = x+i
        y2 = y+i
        if x2 > width-1 or x2 < needed-1 or y2 > height-1 or y2 < needed-1: 
            # would go over the board
            continue
        line = []
        for j in range(needed):
            line.append((x2-j,y2-j))
        if (x,y) in line:
            line.remove((x,y))
        d1lines.append(line)


    # Diagonal lines, upright to downleft. Base moves downleft.
    d2lines = []
    for i in range(needed):
        x2 = x-i
        y2 = y+i
        if x2 < 0 or (x2+needed-1) > width-1 or y2 > height-1 or y2 < needed-1: 
            # would go over the board
            continue
        line = []
        for j in range(needed):
            line.append((x2+j,y2-j))
        if (x,y) in line:
            line.remove((x,y))
        d2lines.append(line)




    print("Vertical lines:")
    for l in vlines:
        print(l)

    print()

    print("Horizontal lines:")
    for l in hlines:
        print(l)

    print()

    print("Diagonal (upleft,downright) lines:")
    for l in d1lines:
        print(l)

    print()

    print("Diagonal (upright,downleft) lines:")
    for l in d2lines:
        print(l)

    print()
