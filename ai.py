import random

class AI:
    def __init__(self,mark):
        self.mark = mark
        self.attack_strategies = []
        self.defence_strategies = []
        f1 = self.vertical_strategies
        f2 = self.horizontal_strategies
        f3 = self.diagonal1_strategies
        f4 = self.diagonal2_strategies
        self.strategy_functions = (f1,f2,f3,f4)

    def update_defence_strategies(self,x,y):
        for strategy in self.defence_strategies:
            if (x,y) in strategy:
                strategy.remove((x,y))


    def update_attack_strategies(self,x,y):
        for strategy in self.attack_strategies:
            if (x,y) in strategy:
                strategy.remove((x,y))


    def delete_attack_strategies(self,x,y):
        a = self.attack_strategies
        self.attack_strategies = [s for s in a if (x,y) not in s]


    def delete_defence_strategies(self,x,y):
        d = self.defence_strategies
        self.defence_strategies = [s for s in d if (x,y) not in s]


    def one_left(self):
        for strategy in self.attack_strategies:
            if len(strategy) == 1:
                return next(iter(strategy)) # Get the only element

        for strategy in self.defence_strategies:
            if len(strategy) == 1:
                return next(iter(strategy)) # Get the only element

        return None


    def attack_defence_union(self):
        # This is unused
        for a_strategy in self.attack_strategies:
            for d_strategy in self.defence_strategies:
                union = a_strategy & d_strategy
                if len(union) > 0:
                    # Get one element from the union set
                    return next(iter(union)) 

        return None


    def shortest_strategy(self,needed):
        if self.attack_strategies and self.defence_strategies:
            # Both not empty
            attack = self.shortest_attack()
            defence = self.shortest_defence()
            shortest_strategy = min(attack,defence,key=len) 

        elif self.attack_strategies and not self.defence_strategies:
            # Defence empty, attack not empty
            shortest_strategy = self.shortest_attack()

        elif self.defence_strategies and not self.attack_strategies:
            # Attack empty, defence not empty
            shortest_strategy = self.shortest_defence()

        if len(shortest_strategy) <= needed // 2 + 1:
            return next(iter(shortest_strategy)) 

        return None


    def shortest_attack(self):
        candidate = self.attack_strategies[0]
        for strategy in self.attack_strategies:
            if len(strategy) < len(candidate):
                candidate = strategy
        return candidate


    def shortest_defence(self):
        candidate = self.defence_strategies[0]
        for strategy in self.defence_strategies:
            if len(strategy) < len(candidate):
                candidate = strategy
        return candidate



    def random_from_strategies(self):
        s = random.choice(self.defence_strategies + self.attack_strategies)
        return random.sample(s,1)[0]


    def random_from_empty_slots(self,board):
        return random.sample(board.empty_slots,1)[0]


    def most_common(self):
        all_coords = []

        for strat in self.attack_strategies + self.defence_strategies:
            all_coords += list(strat)

        most_common = all_coords[0]
        most_common_amount = all_coords.count(most_common)

        for candidate in all_coords:
            candidate_amount = all_coords.count(candidate)
            if candidate_amount > most_common_amount:
                most_common = candidate
                most_common_amount = candidate_amount

        if most_common_amount == 1:
            return None

        return most_common


    def make_decision(self,needed,board):
        if not self.attack_strategies and not self.defence_strategies:
            # Both strategies empty
            return self.random_from_empty_slots(board)

        move = self.one_left()
        if move is not None:
            return move

        move = self.shortest_strategy(needed)
        if move is not None:
            return move

        move = self.most_common()
        if move is not None:
            return move

        return self.random_from_strategies()
    

    def make_a_move(self,board,needed,x,y):
        self.delete_attack_strategies(x,y)
        self.update_defence_strategies(x,y)
        self.new_defence_strategies(board,needed,x,y)
        
        move = self.make_decision(needed,board)

        self.delete_defence_strategies(move[0],move[1])
        self.update_attack_strategies(move[0],move[1])
        self.new_attack_strategies(board,needed,move[0],move[1])

        return move


    def new_defence_strategies(self,board,needed,x,y,):
        for f in self.strategy_functions:
            for strategy in f(board,needed,x,y):
                self.defence_strategies.append(strategy)


    def new_attack_strategies(self,board,needed,x,y,):
        for f in self.strategy_functions:
            for strategy in f(board,needed,x,y):
                self.attack_strategies.append(strategy)



    def vertical_strategies(self,board,needed,recentX,recentY):
        # Vertical strategies. Base moves down
        strategies = []
        for i in range(needed):
            y = recentY+i
            strategy = set()
            
            for j in range(needed):
                strategy.add((recentX,y-j))
            strategy.remove((recentX,recentY))

            for coord in strategy:
                if coord not in board.empty_slots:
                    break
            else:
                strategies.append(strategy)

        return strategies


    def horizontal_strategies(self,board,needed,recentX,recentY):
        # Horizontal strategies. Base moves left.
        strategies = []
        for i in range(needed):
            x = recentX-i
            strategy = set()

            for j in range(needed):
                strategy.add((x+j,recentY))
            strategy.remove((recentX,recentY))

            for coord in strategy:
                if coord not in board.empty_slots:
                    break
            else:
                strategies.append(strategy)
            
        return strategies


    def diagonal1_strategies(self,board,needed,recentX,recentY):
        # Diagonal strategies. Base moves downleft.
        strategies = []
        for i in range(needed):
            x = recentX-i
            y = recentY+i
            strategy = set()

            for j in range(needed):
                strategy.add((x+j,y-j))
            strategy.remove((recentX,recentY))

            for coord in strategy:
                if coord not in board.empty_slots:
                    break
            else:
                strategies.append(strategy)

        return strategies


    def diagonal2_strategies(self,board,needed,recentX,recentY):
        # Diagonal strategies. Base moves downright.
        strategies = []
        for i in range(needed):
            x = recentX+i
            y = recentY+i
            strategy = set()

            for j in range(needed):
                strategy.add((x-j,y-j))
            strategy.remove((recentX,recentY))

            for coord in strategy:
                if coord not in board.empty_slots:
                    break
            else:
                strategies.append(strategy)

        return strategies

