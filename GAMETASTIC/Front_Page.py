import time, random
import pygame,sys, os
from tkinter import filedialog
from tkinter import *
from SlidePuzzle import *
from random import shuffle
from game2048 import *
#from rock_paper_scissors import *

#from tictactoe import *


def func1():
    exec(open('SlidePuzzle.py').read())

def func2():
    import fruit_ninja
    exec(open('fruit_ninja.py').read())

def func3():
    exec(open('tictactoe.py').read())

def func4():
    exec(open('game2048.py').read())

def func5():
    exec(open('hangman.py',encoding="utf8").read())

def func6():
    exec(open('fate.py').read())

def func7():
    import rock_paper_scissors
    exec(open('rock_paper_scissors.py').read())


disp=Tk()
disp.title("GAME CONSOLE")
disp.geometry('800x800+400+10')
disp.configure(bg='grey')


l1=Label(disp, text="GAMETASTIC",font=("Bradley Hand ITC",70,"bold","underline"),bg='grey',fg='black')
l1.pack()

l2=Label(disp, text="WELCOME TO THE VIRTUAL WORLD",font=("Times New Roman",20,"italic"),bg='grey',fg='black')
l2.pack()

p1=PhotoImage(file= r"hangman.png").subsample(2,2)
b1=Button(disp, text="HANGMAN",font=("Agency FB",20,"underline"),bg='yellow',fg='black',image=p1,compound=TOP,command=func5)
b1.place(x=40,y=190)

p2=PhotoImage(file= r"2048.png").subsample(2,2)
b2=Button(disp, text="2048",font=("Agency FB",20,"underline"),bg='yellow',fg='black',image=p2,compound=TOP,command=func4)
b2.place(x=550, y=190)

p3=PhotoImage(file= r"choices.png").subsample(3,3)
b3=Button(disp, text="FATE AT CHOICES",font=("Agency FB",20,"underline"),bg='light blue',fg='black',image=p3,compound=TOP,command=func6)
b3.place(x=40,y=430)

p4=PhotoImage(file= r"puzzle.png").subsample(3,5)
b4=Button(disp, text="SLIDING PUZZLE",font=("Agency FB",20,"underline"),bg='sea green',fg='black',image=p4,compound=TOP,command=func1)
b4.place(x=220,y=190)

p5=PhotoImage(file= r"rock.png").subsample(3,4)
b5=Button(disp, text="ROCK-PAPER",font=("Agency FB",20,"underline"),bg='brown',fg='black',image=p5,compound=TOP,command=func7)
b5.place(x=240,y=430)

p6=PhotoImage(file= r"ninja.png").subsample(3,3)
b6=Button(disp, text="FRUIT NINJA",font=("Agency FB",20,"underline"),bg='light blue',fg='black',image=p6,compound=TOP,command=func2)
b6.place(x=540,y=430)

p7=PhotoImage(file= r"exit.png").subsample(3,4)
b7=Button(disp,text="    E X I T  ",font=("Algerian",30,"bold"),bg='grey',fg='black',image=p7,compound=LEFT,command=disp.destroy)
b7.place(x=230,y=710)

'''
p8=PhotoImage(file= r".png").subsample(,)
b8=Button(disp, text="TIC-TAC-TOE",font=("Agency FB",20,"underline"),bg='light blue',fg='black',image=p8,compound=TOP,command=func3)
b8.place(x=,y=)
'''

disp.mainloop()


