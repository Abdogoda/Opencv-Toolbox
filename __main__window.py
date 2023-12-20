import customtkinter as ctk
from __window__header import *
from __window__canvas import *

class Window(ctk.CTkFrame):
  def __init__(self, master, relx, relwidth, show_sidebar, is_image, image_extension, import_fun, resize_image, export_fun, crop_var, crop_func, draw_var, draw_func, text_var, text_func, draw_size, draw_color, edit_flag, undo_func, save_func):

    # setup
    super().__init__(master=master, fg_color='transparent', corner_radius=0)

    # animation logic
    self.show_sidebar = show_sidebar
    self.start_point = relx
    self.width = relwidth
    self.pos = relx

    # layout
    self.place(relx=relx, rely=0, relwidth=relwidth, relheight=1, anchor='nw')

    # widget
    self.window_header = WindowHeader(self, show_sidebar, is_image, image_extension, import_fun, export_fun, edit_flag, undo_func, save_func)
    self.window_canvas = WindowCanvas(self, is_image, resize_image, crop_var, crop_func, draw_var, draw_func, text_var, text_func, draw_size, draw_color)

  # --- Show Image ---
  def show_image(self, tk_image, img_dimns):
    self.image_window = self.window_canvas.create_image(0, 0, image=tk_image, anchor='nw')
    self.window_canvas.image = tk_image
    self.window_canvas.configure(scrollregion=(0,0,img_dimns[0], img_dimns[1]))

  # --- Destroy Image ---
  def destroy_all(self):
    self.window_canvas.delete('all')

  # --- Draw Grid ---
  def draw_grid(self, width, height):
    for line in range(0, width, 10):
      self.window_canvas.create_line([(line, 0), (line, height)], fill='#666666', tags='grid_line_w')

    for line in range(0, height, 10):
      self.window_canvas.create_line([(0, line), (width, line)], fill='#666666', tags='grid_line_h')

  # --- animation ---
  def animate(self):
    if self.show_sidebar.get(): 
      self.animate_forward()
    else:
      self.animate_backward()

  def animate_forward(self):
    self.pos = 0
    self.width = 1
    self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1, anchor='nw')

  def animate_backward(self):
    self.pos = self.start_point
    self.width = self.width - self.start_point
    self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1, anchor='nw')

  def show_hide_undo(self):
    self.window_header.show_hide_undo()