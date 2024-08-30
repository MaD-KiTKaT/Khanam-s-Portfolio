from tkinter import *
 
root = Tk()
root.geometry("1240x1000")
root.title("My to-do list!")
root.configure(background='black')
 
Label(root, text="To-Do list!!!", font=('Helvetica bold', 25), fg="green").pack(pady=20)
 
def disable_button():
    txt_output.config(state=DISABLED)


 
my_list = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
 
txt_output = Text(root, height=30, width=90)
txt_output.pack(pady=30)
 
for item in my_list:
   txt_output.insert(END, "- " + item + "\n")
 
root.mainloop()
