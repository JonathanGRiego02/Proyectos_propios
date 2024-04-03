import PIL.Image
import cv2
import tkinter as tk
from PIL import Image, ImageTk

# lista de los caracteres que usaremos para representar la foto
ASCII_CHAR = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]
#ASCII_CHAR = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 200):
  width, heigh = image.size
  ratio = heigh / width
  new_heigh = int(new_width * ratio)
  resize_image = image.resize((new_width,new_heigh))
  return resize_image

def grayimage(image):
  gray_image = image.convert("L")
  return gray_image

def PixelToAscii(image):
	pixels = image.getdata() 
	#characters = "".join([ASCII_CHAR[pixel // 25] for pixel in pixels])
	characters = "".join([ASCII_CHAR[min(pixel // (256 // len(ASCII_CHAR)), len(ASCII_CHAR) - 1)] for pixel in pixels])
	return characters


def Image_to_text(image, new_width = 200):
  new_image_data = PixelToAscii(grayimage(resize(image)))
  pixel_count = len((new_image_data))
  ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
  return ascii_image