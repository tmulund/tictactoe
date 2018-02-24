import sys

def test_ai_strategies(ai,x,y):
    # Tests wether ai updated its strategies correctly
    for strategy in ai.defence_strategies:
        if (x,y) in strategy:
            print("Error in ai defence strategies")
            print("This shouldn't be here: "+  str((x,y)))
            sys.exit()

    for strategy in ai.attack_strategies:
        if (x,y) in strategy:
            print("Error in ai attack strategies")
            print("This shouldn't be here: "+  str((x,y)))
            sys.exit()
