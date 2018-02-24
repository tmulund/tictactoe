import board
from util import ask_coordinates, check_victory, check_tie
import ai
import tests
import time

# ---- Initialize game ------
board = board.Board(10,10)
needed = 5
ai1 = ai.AI("O")
ai2 = ai.AI("X")

x = 0
y = 0

while True:
    time.sleep(0.5)

    # ----- X's turn ------
    (x,y) = ai2.make_a_move(board,needed,x,y)
    tests.test_ai_strategies(ai2,x,y)

    board.update(x,y,"X")
    board.print_self()
    print()

    if check_tie(board) == True:
        print("Tie")
        break

    if check_victory(board,x,y,needed) == True:
        print("A.I. 2 wins")
        print("Last move:  " + str((x,y)))
        break


    time.sleep(0.5)

    # ------ O's turn -----
    (x,y) = ai1.make_a_move(board,needed,x,y)
    tests.test_ai_strategies(ai1,x,y)

    board.update(x,y,"O")
    board.print_self()
    print()

    if check_tie(board) == True:
        print("Tie")
        break

    if check_victory(board,x,y,needed) == True:
        #board.print_self()
        print("A.I. 1 wins")
        print("Last move:  " + str((x,y)))
        break



