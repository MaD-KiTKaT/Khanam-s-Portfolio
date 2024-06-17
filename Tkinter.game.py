#Run Module!
import tkinter as tk
import random
import keyboard


#~~~~THIS IS FOR THE ACTUAL BOX~~~~~#

window = tk.Tk()
#Create a window for tkinter

window.geometry("500x500")
#What window size you want

window.title("Maths Quiz! :D")
#You can use this function to set the title!



#~~~~THIS IS ALL THE CODE USED TO CREAT THE BOX FOR USER INPUT~~~~#

#Assignsthe variable to a class (makes it easy to monitor)
Answer_var = tk.StringVar()

#def is a keyword used to define a function
def submit():
#This retrieves the answer from the individual 
    Answer=Answer_var.get()
    Answer_var.set("")
#   ^^^^^^^^^^^^^^^^^Is like a box which holds different values, it sets it empty!

#This displays the text "answer". You can change the font, size and Style!
Ans_label = tk.Label(text='Answer:', font=('calibre', 10, 'bold'))
#This assigns variable 'Ans_var' to a class (makes it easier to monitor)
Ans_var = tk.StringVar()
#This creates the text box which the user can input text in. It sets the font, size and style the text shows up in!
Ans_entry = tk.Entry(textvariable=Ans_var, font=('calibre', 10, 'normal'))
#This creates the submit button, names it and commands it to send the info inputted to the specified place.
sub_btn = tk.Button(text='Submit', command=submit)

#This is all to specify where to place the button/box/text
Ans_label.grid(row=2, column=1)
Ans_entry.grid(row=2, column=2)
sub_btn.grid(row=2, column=4)


#~~~~THIS IS FOR THE MATHS QUESTIONS~~~~#
while True:
    
        if keyboard.is_pressed("s"):

            print("You pressed s.")

            break


#This orders for the game to fully start

window.mainloop()
