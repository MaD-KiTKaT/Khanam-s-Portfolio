import random
import tkinter as tk
import string

#Set the geometry
window = tk.Tk()
#Create a window for tkinter

window.geometry("500x500")
#What window size you want

window.title("Password Generator :D")
#You can use this function to set the title!

# Create a label
Context = tk.Label(window, text="Generate a random password:D ").place(x = 60, y = 80)
# You can customize the label by specifying additional properties such as font, color, etc.
BUTTON = tk.Button(window , text = "Generate")
BUTTON.place(x = 240, y = 90)
textbox = tk.Text(window, height=2, width=40)
textbox.place(x=75, y=125)
textbox.configure(state="disabled")

# Example text to be displayed
Num = string.digits
n = random.randint(0,100)

lo = string.ascii_lowercase
num_lo = 5
ran_lo = random.choices(lo, k=num_lo)

l = string.ascii_uppercase
num_l = 5
ran_up = random.choices(l, k=num_l)

Sym = string.punctuation
length = 6
PASS = random.sample(lo, length) + random.sample(Num, length) + random.sample(l, length)
# Insert text into the textbox
textbox.configure(state="normal")
textbox.delete("1.0", tk.END)
textbox.insert(tk.END, PASS)
textbox.configure(state="disabled")
# Disable editing in the textbox
BUTTON = tk.Button(window , text="Generate", command=generate_password)
BUTTON.place(x=240, y=90)


window.mainloop()
