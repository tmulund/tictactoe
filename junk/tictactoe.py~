import board
from util import ask_coordinates, check_victory
import ai
import tests

board = board.Board(10,10)
needed = 5
ai = ai.AI("O")

def print_ai_strategies(ai):
    print()
    print("Defence srategies")
    for d in ai.defence_strategies:
        print(d)
    print()

    print("Attack srategies")
    for a in ai.attack_strategies:
        print(a)
    print()


while True:
    # ----- X's turn ------
    board.print_self()
    (x,y) = ask_coordinates(board)
    board.update(x,y,"X")

    if check_victory(board,x,y,needed) == True:
        board.print_self()
        print("Player wins")
        break


    # ------ O's turn -----
    #print_ai_strategies(ai)
    (x,y) = ai.make_a_move(board,needed,x,y)
    board.update(x,y,"O")

    print()
    print("AI made move: " + str((x,y)))
    print()
    tests.test_ai_strategies(ai,x,y)

    if check_victory(board,x,y,needed) == True:
        board.print_self()
        print("A.I. wins")
        break
