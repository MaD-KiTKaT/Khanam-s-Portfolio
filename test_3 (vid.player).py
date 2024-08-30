import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import imageio
import threading

class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.video_path = video_path
        self.video_label = Label(root)
        self.video_label.pack()
        self.video = imageio.get_reader(r"C:\Users\RPC-K\Downloads\windows 95 maze screensaver 022 speedrun  [WORLD RECORD].mp4")
        self.play_video = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def update(self):
        for frame in self.video.iter_data():
            if not self.play_video:
                break
            image = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image)
            self.video_label.config(image=image)
            self.video_label.image = image
            self.root.update()
        self.video.close()

    def stop(self):
        self.play_video = False
        self.thread.join()

def on_close():
    player.stop()
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Video Player")
    video_path = 'path_to_your_video.mp4'
    player = VideoPlayer(root, video_path)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
