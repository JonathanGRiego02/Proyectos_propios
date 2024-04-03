import cv2
import tkinter as tk
from PIL import Image, ImageTk

ASCII_CHAR = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]

def resize(image, new_width=200):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resize_image = image.resize((new_width, new_height))
    return resize_image

def grayimage(image):
    gray_image = image.convert("L")
    return gray_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHAR[min(pixel // (256 // len(ASCII_CHAR)), len(ASCII_CHAR) - 1)] for pixel in pixels])
    return characters

def update_ascii_image(cap, label, root):
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = resize(img)
    img = grayimage(img)
    ascii_image = pixel_to_ascii(img)
    pixel_count = len(ascii_image)
    ascii_image_display = "\n".join(ascii_image[i:(i+80)] for i in range(0, pixel_count, 80))

    label.config(text=ascii_image_display)

    imgtk = ImageTk.PhotoImage(img)
    label.imgtk = imgtk
    label.config(image=imgtk)

    root.after(10, update_ascii_image, cap, label, root)

def main():
    root = tk.Tk()
    root.title("ASCII Art Webcam Viewer")

    label = tk.Label(root, font=('Monaco', 8), anchor='nw', justify='left')
    label.pack(expand='true', fill='both')

    cap = cv2.VideoCapture(0)  # Cambia el 0 a 1 o 2 si tienes múltiples cámaras

    update_ascii_image(cap, label, root)

    root.mainloop()

    cap.release()

if __name__ == "__main__":
    main()


import PIL.Image

