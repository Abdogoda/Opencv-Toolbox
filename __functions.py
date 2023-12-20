import customtkinter as ctk
from __settings import *
from PIL import Image, ImageTk


def image_icon(image_tuple):
 image = ctk.CTkImage(light_image=Image.open(image_tuple[1]), dark_image=Image.open(image_tuple[0]), size=(24, 24))
 return image


def image_colored_icon(colored_path):
 image = ctk.CTkImage(Image.open(colored_path), size=(24, 24))
 return image