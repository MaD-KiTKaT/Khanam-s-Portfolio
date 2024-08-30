import tkinter as tk
from tkinter import ttk
import cv2
import threading
import tkVideoPlayer

class VideoPlayer:
    def __init__(self, master, video_path):
        self.master = master
        self.video_path = video_path

        # Create a frame for the video player
        self.video_frame = tk.Frame(master)
        self.video_frame.pack()

        # Create a label to display the video
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()

        # Create a play button
        self.play_button = ttk.Button(self.video_frame, text="Play", command=self.play_video)
        self.play_button.pack(side="left")

        # Create a pause button
        self.pause_button = ttk.Button(self.video_frame, text="Pause", command=self.pause_video)
        self.pause_button.pack(side="left")

        # Create a stop button
        self.stop_button = ttk.Button(self.video_frame, text="Stop", command=self.stop_video)
        self.stop_button.pack(side="left")

        # Initialize the video capture object
        self.cap = cv2.VideoCapture(self.video_path)

        # Set the initial state of the player
        self.playing = False
        self.paused = False

    def play_video(self):
        self.playing = True
        self.paused = False

        # Start a new thread to handle the video playback
        thread = threading.Thread(target=self.update_video)
        thread.daemon = True
        thread.start()

    def pause_video(self):
        self.paused = True

    def stop_video(self):
        self.playing = False
        self.paused = False
        self.cap.release()

    def update_video(self):
        while self.playing:
            ret, frame = self.cap.read()

            # If the video has reached the end, stop playback
            if not ret:
                self.playing = False
                self.cap.release()
                break

            # Convert the frame to a photo image
            photo = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            self.video_label.config(image=photo)
            self.video_label.image = photo

            # Check if paused
            if self.paused:
                while self.paused:
                    pass

            # Update the display every 30 milliseconds
            self.video_label.after(30)

# Create the main window
root = tk.Tk()
root.title("Video Player")

# Create the video player object
video_player = VideoPlayer(root, "C:/Users/RPC-K/Downloads/11920521_3840_2160_60fps.mp4")

# Run the main loop
root.mainloop()
