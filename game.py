from tkinter import * 
import board, ai

class Game:
    def __init__(self,height,width,needed):
        self.board = board.Board(height,width)
        self.ai = ai.AI("O")
        self.height = height
        self.width = width
        self.needed = needed
        self.window = Toplevel()
        self.window.withdraw()

        # Playable buttons
        self.buttons = {}  
        self.create_buttons(self.window,self.height,self.width)

        # Label for winner
        self.win_label = Label(self.window, text="", justify=CENTER)
        self.win_label.grid(row=self.height, columnspan=width)

        # Quit button
        quit_btn = Button(self.window, text="Quit Game", 
                    command=self.window.destroy)
        quit_btn.grid(row=self.height+1, columnspan=5)

        # Restart button
        restart_btn = Button(self.window, text="Restart Game",
                    command=self.restart_function)
        restart_btn.grid(row=self.height+1, column=5, columnspan=5)


    def restart_function(self):
        # Create new board and ai objects
        self.board = board.Board(self.height,self.width)
        self.ai = ai.AI("O")

        # Configure buttons for new game
        for btn in self.buttons.values():
            pic = PhotoImage(file="./empty.ppm")
            btn.img = pic 
            btn.config(image=pic, state=NORMAL)

        # Empty winner label
        self.win_label.config(text="")


    def button_function(self,btn):
        def f():
            self.turn(btn.coord[0],btn.coord[1],"X")
        return f

    def create_buttons(self,window,height,width):
        for y in range(height):
            for x in range(width):

                pic = PhotoImage(file="./empty.ppm")
                btn = Button(self.window, image=pic, height=20, width=20)
                btn.img = pic 
                btn.grid(row=y, column=x)
                btn.coord = (x,y)
                
                f = self.button_function(btn)
                btn.config(command=f)

                self.buttons[(x,y)] = btn

    
    def turn(self,x,y,mark):
        # Players move
        self.board.update(x,y,mark)
        self.update_button(mark,x,y)
        player_wins = self.board.check_victory(x,y,self.needed)
        is_tie = self.board.check_tie()

        if player_wins:
            self.disable_buttons()
            self.win_label.config(text="Player Wins!")
        elif is_tie:
            self.disable_buttons()
            self.win_label.config(text="Tie!")

        # Computer makes move only if player didn't just win
        if not player_wins and not is_tie:
            (x,y) = self.ai.make_a_move(self.board,self.needed,x,y)
            self.board.update(x,y,self.ai.mark)
            self.update_button(self.ai.mark,x,y)

            if self.board.check_victory(x,y,self.needed) == True:
                self.win_label.config(text="Computer wins!")
                self.disable_buttons()

            elif self.board.check_tie() == True:
                self.win_label.config(text="Tie!")
                self.disable_buttons()


    def update_button(self,mark,x,y):
        btn = self.buttons[(x,y)]
        if mark == "X":
            pic = PhotoImage(file="./x.ppm")
        elif mark == "O":
            pic = PhotoImage(file="./o.ppm")
        btn.config(image=pic, state=DISABLED)
        btn.img = pic


    def disable_buttons(self):
        for btn in self.buttons.values(): 
            btn.config(state=DISABLED)


    def launch_game(self):
        self.window.deiconify()
        
