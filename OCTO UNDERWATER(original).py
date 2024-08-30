import tkinter as tk
from PIL import Image, ImageTk
import random

def move_image(event):
    x = max(0, min(event.x, canvas_width - image_width))
    canvas.coords(image_id, x, 755 - image_height)

def create_falling_image():
    mini_image = Image.open(coin).resize((50, 50), Image.LANCZOS)
    mini_photo_image = ImageTk.PhotoImage(mini_image)
    x = random.randint(0, canvas_width - 30)
    mini_image_id = canvas.create_image(x, 0, anchor=tk.NW, image=mini_photo_image)
    falling_images.append((mini_image_id, mini_photo_image))
    root.after(500, create_falling_image)
score = 0
def update_falling_images():
    global score
    for image_id, _ in falling_images:
        x, y = canvas.coords(image_id)
        if y < canvas_height:
            canvas.move(image_id, 0, 5)
            if check_collision(image_id):
                canvas.delete(image_id)
                falling_images.remove((image_id, _)) 
                score += 1      
        else:
            canvas.delete(image_id)
            falling_images.remove((image_id, _))
    root.after(50, update_falling_images)


    
def check_collision(mini_image_id):
    main_bbox = canvas.bbox(image_id)
    mini_bbox = canvas.bbox(mini_image_id)
    return intersect(main_bbox, mini_bbox)

def intersect(bbox1, bbox2):
    return not (bbox1[2] < bbox2[0] or bbox1[0] > bbox2[2] or
                bbox1[3] < bbox2[1] or bbox1[1] > bbox2[3])


root = tk.Tk()
root.title("OCTO-COIN (by Khanam)")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


bg_image_path = r"C:/Users/RPC-K/OneDrive/Pictures/images.jfif"
bg_image = Image.open(bg_image_path).resize((1532, 805), Image.LANCZOS)
bg_photo_image = ImageTk.PhotoImage(bg_image)


canvas_width = screen_width
canvas_height = screen_height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=tk.BOTH, expand=True)


canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_image)


fg_image_path = r"C:/Users/RPC-K/Downloads/pngtree-cute-cartoon-octopus-clipart-png-image_2678888-removebg-preview.png"
fg_image = Image.open(fg_image_path).resize((150, 150), Image.LANCZOS)
fg_photo_image = ImageTk.PhotoImage(fg_image)


image_id = canvas.create_image(0, canvas_height - 100, anchor=tk.NW, image=fg_photo_image)
image_width = 100
image_height = 100


canvas.config(scrollregion=canvas.bbox(tk.ALL))

# Bind the mouse movement to the move_image function
canvas.bind('<Motion>', move_image)


coin = r"C:/Users/RPC-K/Downloads/images__1_-removebg-preview.png"

#Keeps track of the falling images
falling_images = []



#Run subroutines
create_falling_image()
update_falling_images()


root.mainloop()
