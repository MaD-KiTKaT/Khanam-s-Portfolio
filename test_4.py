from tkVideoPlayer import TkinterVideo
import tkinter as tk
from pathlib import Path
 
path = Path(__file__).parent
 
 
root = tk.Tk()
root.geometry('800x600+200+200')
 
file = r"C:\Users\RPC-K\Downloads\windows 95 maze screensaver 022 speedrun  [WORLD RECORD].mp4"
 
player = TkinterVideo(root, scaled=True)
player.pack(expand=True, fill='both')
player.load(file)
 
player.play()
 
play = tk.Button(root, text='Play', command=player.play)
play.pack(side='left', padx=4, pady=8)
 
pause = tk.Button(root, text='Pause', command=player.pause)
pause.pack(side='left', padx=4, pady=8)
 
stop = tk.Button(root, text='Close', command=player.stop)
stop.pack(side='left', padx=4, pady=8)
root.mainloop()
