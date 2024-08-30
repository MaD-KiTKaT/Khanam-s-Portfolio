import tkinter as tk
from PIL import Image, ImageTk
import imageio
import pygame


class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.video_label = tk.Label(root)
        self.video_label.pack()
        self.video = imageio.get_reader(video_path)
        self.play_video = True
        self.frame_iter = self.video.iter_data()
        self.update()
 
    def update(self):
        if self.play_video:
            self.root.after(120, self.update)  # call update again after 1/320 of a second.
            try:
                frame = next(self.frame_iter)
                image = Image.fromarray(frame).resize((1400, 800))
                image = ImageTk.PhotoImage(image)
                self.video_label.config(image=image)
                self.video_label.image = image
                self.root.update()
            except StopIteration:
                self.play_video = False
        else:
            self.video.close()
            root.destroy()
 
    def stop(self):
        self.play_video = False
        

 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Video Player")
    video_path = r"C:\\Users\\RPC-K\\OneDrive\\Pictures\\Camera imports\\2023-3-5\\windows 95 maze screensaver 022 speedrun  [WORLD RECORD].mp4"
    player = VideoPlayer(root, video_path)
    root.protocol("WM_DELETE_WINDOW", player.stop)

    
    root.mainloop()
