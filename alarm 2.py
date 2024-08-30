from tkinter import *
import datetime
import time
import winsound
from threading import *
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("600x600")
 
# Function to draw background shapes and lines
def draw_background(canvas):
    # Draw a rectangle for background
    canvas.create_rectangle(0, 0, 600, 400, fill="lightblue", outline="")
 
    # Draw sun
    canvas.create_oval(500, 50, 550, 100, fill="yellow", outline="")
 
    # Draw mountains
    canvas.create_polygon(0, 250, 150, 100, 300, 250, fill="gray", outline="")
 
    # Draw grass
    canvas.create_rectangle(0, 300, 600, 400, fill="green", outline="")
 
    # Draw a tree
    canvas.create_rectangle(400, 200, 420, 300, fill="brown", outline="")
    canvas.create_oval(360, 150, 460, 250, fill="green", outline="")
 
# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    # Infinite Loop
    while True:
        # Set Alarm 
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("*", winsound.SND_ASYNC)
 
# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()
 
# Create a canvas for drawing background
canvas = Canvas(root, width=600, height=400)
canvas.pack()
 
# Draw the background
draw_background(canvas)
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = tuple(f"{i:02}" for i in range(25))  # Using tuple comprehension for hours
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(61))  # Using tuple comprehension for minutes and seconds
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(61))
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)
 
# Execute Tkinter
root.mainloop()
 
