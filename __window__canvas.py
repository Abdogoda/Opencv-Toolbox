import customtkinter as ctk
from __settings import * 
from tkinter import Canvas
from PIL import Image, ImageTk

class WindowCanvas(Canvas):
  def __init__(self, parent, is_image, resize_image, crop_var, crop_func, draw_var, draw_func, text_var, text_func, draw_size, draw_color):

    # setup
    super().__init__(
    master=parent, 
    bd=0, 
    highlightthickness=0, 
    bg="#999999",
    relief='ridge', 
    scrollregion=(0,0,0,0))
    self.config(cursor="crosshair")
    self.place(relx=0, rely=0.07, relwidth=1, relheight=0.93)

    self.crop_var = crop_var
    self.draw_var = draw_var
    self.text_var = text_var
    self.crop_var.trace('w', self.cropping_func)
    self.draw_var.trace('w', self.drawing_func)
    self.text_var.trace('w', self.texting_func)
    self.crop_func = crop_func
    self.draw_func = draw_func
    self.text_func = text_func

    self.start_x = None
    self.start_y = None
    self.rect_id = None
    self.circle_id = None

    self.draw_color = draw_color
    self.draw_size = draw_size
    self.draw_color.trace('w', self.update_color)
    self.draw_size.trace('w', self.update_size)
    self.color = self.update_color()
    self.size = self.update_size()
    self.drawing = False
    self.points = []
    self.text_id = None
    self.bind('<Configure>', lambda event: resize_image(event))
    self.bind('<MouseWheel>', lambda event:self.yview_scroll(-int(event.delta/60), "units"))
    self.bind('<Control MouseWheel>', lambda event:self.xview_scroll(-int(event.delta/60), "units"))

  # croppping function
  def cropping_func(self, *args):
    if self.crop_var.get() != CROP_OPTIONS[0]:
      self.bind("<ButtonPress-1>", self.on_press)
      self.bind("<B1-Motion>", self.on_drag)
      self.bind("<ButtonRelease-1>", self.on_release)
    else:
      self.crop_func({})

  def on_press(self, event, *args):
    self.start_x = self.canvasx(event.x)
    self.start_y = self.canvasy(event.y)
    self.delete("rectangle")
    self.delete("circle")

  def on_drag(self, event, *args):
    cur_x = self.canvasx(event.x)
    cur_y = self.canvasy(event.y)

    if self.rect_id:
      self.delete(self.rect_id)

    if self.circle_id:
      self.delete(self.circle_id)

    if self.crop_var.get() == 'Rect':
      self.rect_id = self.create_rectangle(self.start_x, self.start_y, cur_x, cur_y, outline="blue", tags="rectangle")
    elif self.crop_var.get() == 'Circle': 
      self.circle_id = self.create_oval(self.start_x, self.start_y, cur_x, cur_y, outline="blue", tags="circle")

  def on_release(self, event, *args):
    end_x = self.canvasx(event.x)
    end_y = self.canvasy(event.y)

    cropping_data = {
    'type' : self.crop_var.get(),
    'coordinates' : [(self.start_x, self.start_y), (end_x, end_y)]
    }
    self.crop_func(cropping_data)


  # drawing function
  def drawing_func(self, *args):
    if self.draw_var.get() != DRAW_OPTIONS[0]:
      if self.draw_var.get() == 'Fill':
        self.draw_func([(0, 1), (0, 1)])
      else:
        self.bind("<Button-1>", self.start_drawing)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.stop_drawing)
    else:
      self.drawing = False
      self.points = []
      self.draw_func(self.points)

  def start_drawing(self, event):
    if self.draw_var.get() != DRAW_OPTIONS[0]:
      self.drawing = True
      self.ix, self.iy = event.x, event.y
      self.points = [(event.x, event.y)]

  def draw(self, event):
    if self.draw_var.get() != DRAW_OPTIONS[0] and self.drawing:
      x, y = event.x, event.y
      self.points.append((x, y))
      self.create_line(self.points, fill=self.color, width=self.size)

  def stop_drawing(self, event):
    if self.draw_var.get() != DRAW_OPTIONS[0]:
      self.drawing = False
      self.draw_func(self.points)
      self.points = []


  # drawing text
  def texting_func(self, *args):
    if self.text_var.get() != '':
      self.bind("<ButtonPress-1>", self.on_text_press)

  def on_text_press(self, event):
    if self.text_id is not None:
      self.delete(self.text_id)
    self.text_position = (event.x, event.y)
    self.text_id = self.create_text(event.x, event.y, text=self.text_var.get())
    self.text_func(self.text_position)



# ---- update color and size ---
  def update_color(self, *args):
    hex_color = self.draw_color.get().lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    self.color = "#{:02x}{:02x}{:02x}".format(*rgb)

  def update_size(self, *args):
    self.size = self.draw_size.get()