from tkinter import *
from random import *
import random
import time
import tkinter as tk
import math
import operator
from tkinter import messagebox


#This is for creating the tkinter window and fixing the specified dimensions into place
root = tk.Tk()
root.geometry("900x600")

#This section creates the canvas and its specifications
canvas_width = 900
canvas_height = 500
c = Canvas(root, width=canvas_width, height=canvas_height, bg="pink")
c.pack()

def quitgame():
    root.destroy()
    
class Game_Images:
    #Background Image
    bg = PhotoImage(file="../Data/sidescroll background flip.gif")
    bg = bg.zoom(2)
    c.create_image(0,0, anchor=NW, image=bg)

    #Insert Image of Enemy
    enemy = PhotoImage(file="../Data/monke2.png")
    enemy1 = c.create_image(0,260, anchor=NW, image=enemy)

    #Insert image of playable character
    player = PhotoImage(file="../Data/monke2.png")
    player1 = c.create_image(0,325, anchor=NW, image=player)
g = Game_Images()


score = 0
x = 1

def game_start():
    global answer, question
    int_1 = random.randint(1, 12)
    int_2 = random.randint(1, 12)
    displayQuestion = "What is "+str(int_1)+ "*" + str(int_2)+"?"
    operator = ["*"]
    ops = random.choice(operator)
    c.create_rectangle(353,0,550,75, fill = "white")
    c.create_text(450, 50, font = ("Helvetica", 15), fill="pink", text = displayQuestion)
    question = str(int_1) + str(ops) + str(int_2)
    answer = int_1 * int_2

def generateQ():
    ans = e1.get()
    e1.delete(0, END)
    if ans == answer:
        score += 1
        x += 1
        print("correct")
        print(ans)
        print(answer)
    else:
        print("wrong")
        print(ans)
        print(answer)


#Buttons show up below the canvas to run commands when pressed
Button(root, text = "Commence Forth",width = 15, command = game_start).place(x=10, y=570)
Button(root, text = "Quit",width = 11, command = quitgame).place(x=800, y=570)
e1 = Entry(root)
e1.pack(padx=30, pady=30)
b=Button(root,text="Enter", width=5, font=("Helvetica", 12), command = generateQ)
b.place(x=550, y=534)

            
root.mainloop()
