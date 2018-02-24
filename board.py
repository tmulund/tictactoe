def create_squares(width,height):
    squares = {}
    for x in range(width):
        for y in range(height):
            squares[(x,y)] = "_"
    return squares


class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.squares = create_squares(width,height)
        self.empty_slots = set(self.squares.keys())
        self.o_coordinates= set()
        self.x_coordinates= set()


    def update(self,x,y,mark):
        self.squares[(x,y)] = mark
        self.empty_slots.remove((x,y))
        if mark == "X":
            self.x_coordinates.add((x,y))
        elif mark == "O":
            self.o_coordinates.add((x,y))


    def print_self(self):
        # Prints the content of the board and numbers around it
        self.print_numbers_above(self.width)

        for y in range(self.width):
            print(y,end=" ") # vertical number

            for x in range(self.height):
                print(self.squares[x,y],end = " ")
            print()


    def print_numbers_above(self,width):
        # prints numbers above the board
        print("  ",end="")
        for n in range(width):
            print(n,end=" ")
        print()


    def check_victory(self,x,y,needed):
        # Checks if there is a winning line 
        if self.squares[(x,y)] == "X":
            coordinates = self.x_coordinates
        elif self.squares[(x,y)] == "O":
            coordinates = self.o_coordinates

        if self.count_vertical(coordinates,x,y) >= needed:
            return True
        elif self.count_horizontal(coordinates,x,y) >= needed:
            return True
        elif self.count_diagonal1(coordinates,x,y) >= needed:
            return True
        elif self.count_diagonal2(coordinates,x,y) >= needed:
            return True
        else:
            return False


    def check_tie(self):
        # Checks if there's a tie
        return len(self.empty_slots) == 0


    def count_upwards(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            y -= 1

        return matches


    def count_downwards(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            y += 1

        return matches


    def count_vertical(self,coordinates,x,y):
        matches = 1 # the one that was just put
        matches += self.count_upwards(coordinates,x,y-1)
        matches += self.count_downwards(coordinates,x,y+1)
        return matches 


    def count_right(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x += 1

        return matches
        

    def count_left(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x -= 1

        return matches


    def count_horizontal(self,coordinates,x,y):
        matches = 1 # the one that was just put
        matches += self.count_right(coordinates,x+1,y)
        matches += self.count_left(coordinates,x-1,y)
        return matches 


    def count_upright(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x += 1
            y -= 1

        return matches


    def count_downleft(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x -= 1
            y += 1

        return matches


    def count_diagonal1(self,coordinates,x,y):
        # from up right to down left
        matches = 1 # the one that was just put
        matches += self.count_upright(coordinates,x+1,y-1)
        matches += self.count_downleft(coordinates,x-1,y+1)
        return matches 


    def count_upleft(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x -= 1
            y -= 1

        return matches


    def count_downright(self,coordinates,x,y):
        matches = 0
        while (x,y) in coordinates:
            matches += 1
            x += 1
            y += 1

        return matches


    def count_diagonal2(self,coordinates,x,y):
        # from up left to down right
        matches = 1 # the one that was just put
        matches += self.count_upleft(coordinates,x-1,y-1)
        matches += self.count_downright(coordinates,x+1,y+1)
        return matches 


