import cv2
from PIL import Image, ImageTk
import tkinter as tk
import PIL.Image

ASCII_CHAR = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]

def resize(image, new_width=100):
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

def imagetotext(image, new_width=100):
    new_image_data = pixel_to_ascii(grayimage(resize(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    return ascii_image

def show_webcam():
    cap = cv2.VideoCapture(0)
    root = tk.Tk()
    root.title("Webcam Viewer")

    text_widget = tk.Text(root, height=100, width=100)
    text_widget.pack()

    # Configura la fuente y el tamaño
    font = ("Courier",8)  # Cambia "Courier" a la fuente que desees y 12 al tamaño deseado
    text_widget.config(font=font)

    def update():
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame)
        
        text = imagetotext(pil_image)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, text)

        photo = ImageTk.PhotoImage(pil_image)
        
        root.after(10, update)

    update()
    root.mainloop()

    cap.release()

if __name__ == "__main__":
    show_webcam()
