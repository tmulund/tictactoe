from tkinter import * 
import game

master = Tk()

# Entry and label for height
e1 = Entry(master)
e1.insert(0,"10") # Default value
e1.grid(row=0,column=1)
l1 = Label(master,text="Height")
l1.grid(row=0,column=0)

# Entry and label for width
e2 = Entry(master)
e2.insert(0,"10") 
e2.grid(row=1,column=1)
l2 = Label(master,text="Width")
l2.grid(row=1,column=0)

# Entry and lable for needed
e3 = Entry(master)
e3.insert(0,"5") 
e3.grid(row=2,column=1)
l3 = Label(master,text="Needed")
l3.grid(row=2,column=0)

# Label for bad inputs
l4 = Label(master,text="",width=9)
l4.grid(row=3,column=0)

def new_game():
    try:
        height = int(e1.get())
        width = int(e2.get())
        needed = int(e3.get())
        if height < 2 or width < 2 or needed < 2:
            raise ValueError
        l4.config(text="")
        new_game = game.Game(height,width,needed)
        new_game.launch_game()
    except ValueError:
        l4.config(text="Bad input")

def quit():
    master.destroy()

new_game_btn = Button(master, text="New game", command=new_game)
new_game_btn.grid(row=3,column=1)

quit_btn = Button(master,text="Quit",command=quit)
quit_btn.grid(row=3,column=2)

master.mainloop()
