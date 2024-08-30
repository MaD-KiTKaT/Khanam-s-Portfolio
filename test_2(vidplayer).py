import tkinter as tk
from PIL import Image, ImageTk
import cv2

root = tk.Tk()

# Create a Canvas widget to display the video
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")

# Load your video file (replace with the actual path to your video)
video_path = r"C:\Users\RPC-K\OneDrive\Pictures\Camera Roll\WIN_20230429_18_50_06_Pro.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

def play_video():
    ret, frame = cap.read()
    if ret:
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert to PIL Image
        pil_image = Image.fromarray(frame_rgb)
        # Convert to PhotoImage
        photo_image = ImageTk.PhotoImage(image=pil_image)
        # Display the frame on the canvas
        canvas.create_image(0, 0, anchor="nw")
    else:
        print("Video playback completed.")
        cap.release()
play_video()

root.mainloop()

