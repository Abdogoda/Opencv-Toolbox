import tkinter as tk
import customtkinter as ctk
from __settings import *
from __functions import *

class CustomMessageBox:
    def __init__(self, master, text, type):
        self.master = master

        # Create a toplevel window
        self.top = tk.Toplevel(master)
        self.top.title("Success")
        self.top.overrideredirect(True)
        self.top.configure(bg=BACKGOUND_COLOR[1])

        # Set the geometry and position it in the center of the screen
        window_width = 300
        window_height = 150
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.top.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        success_icon = image_colored_icon(SUCCESS_IMAGE['colored'])
        warning_icon = image_colored_icon(WARNING_IMAGE['colored'])
        info_icon = image_colored_icon(INFO_IMAGE['colored'])
        if type == 'success':
            ctk.CTkLabel(self.top, text='Success ', text_color=MAIN_COLOR, image=success_icon, compound='right', font=("Helvetica", 28), fg_color='transparent').pack(pady=10)
        elif type == 'warning':
            ctk.CTkLabel(self.top, text='Warning ', text_color=MAIN_COLOR, image=warning_icon, compound='right', font=("Helvetica", 28), fg_color='transparent').pack(pady=10)
        elif type == 'info':
            ctk.CTkLabel(self.top, text='Info ', text_color=MAIN_COLOR, image=info_icon, compound='right', font=("Helvetica", 28), fg_color='transparent').pack(pady=10)

        ctk.CTkLabel(self.top, text=text, font=("Helvetica", 18), fg_color='transparent', text_color=LIGHT[0]).pack(pady=10)

        ctk.CTkButton(self.top, text="OK", border_width=1, border_color=MAIN_COLOR, fg_color='transparent', hover_color=MAIN_COLOR, border_spacing=5, corner_radius=0, command=self.top.destroy).pack(side='bottom', pady=10)


class TopLevelDetection:
    def __init__(self, master, text, image, save_func):
        self.master = master

        # Create a toplevel window
        self.top = tk.Toplevel(master)
        self.top.title(text)
        self.top.overrideredirect(True)
        self.top.configure(bg=BACKGOUND_COLOR[1])

        # Set the geometry and position it in the center of the screen
        window_width = 500
        window_height = 500
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.top.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        ctk.CTkLabel(self.top, text='', image=image).pack(fill='both', expand=True, padx=5, pady=10)
        ctk.CTkButton(
            self.top, 
            text='Save',
            border_width=1, 
            fg_color=MAIN_COLOR, 
            hover_color=SECOND_COLOR, 
            text_color=LIGHT,
            border_spacing=5, 
            corner_radius=0,
            compound='right',
            command=save_func).pack(side='left', expand=True, padx=5, pady=10)
        ctk.CTkButton(
            self.top, 
            text="Cancel", 
            border_width=1, 
            fg_color=MAIN_COLOR, 
            hover_color=SECOND_COLOR, 
            text_color=LIGHT,
            border_spacing=5, 
            corner_radius=0, 
            command=self.top.destroy).pack(side='left', expand=True, padx=5, pady=10)