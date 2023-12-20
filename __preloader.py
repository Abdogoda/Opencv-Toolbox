import customtkinter as ctk
from tkVideoPlayer import TkinterVideo
from __settings import *

class Preloader(ctk.CTkFrame):
 def __init__(self, master, callback):
  super().__init__(master=master, fg_color='transparent', corner_radius=0)
  self.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')

  video_player = TkinterVideo(master=self, scaled=True)
  video_player.load(PRELOADER_PATH)
  video_player.pack(expand=True, fill="both")
  video_player.play()

  self.after(5500, callback)