import customtkinter as ctk
from __settings import *
from __panels import *

class Controlbar(ctk.CTkFrame):
  def __init__(self, master, relx, relwidth, show_sidebar, control_panel, data_vars, draw_color, draw_size):

    # setup
    super().__init__(master=master, fg_color=CONTROL_COLOR, corner_radius=0)

    # animation logic
    self.show_sidebar = show_sidebar
    self.start_point = relx
    self.width = relwidth
    self.pos = relx

    # layout
    self.place(relx=relx, rely=0, relwidth=relwidth, relheight=1, anchor='nw')

    self.panels_frame = ctk.CTkFrame(self, fg_color='transparent')
    self.panels_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # --- POSITION ---
    if control_panel.get() == 0:
      PositionFrame(self.panels_frame, data_vars)
    # --- COLORS ---
    elif control_panel.get() == 1:
      ColorsFrame(self.panels_frame, data_vars)
    # --- EFFECTS ---
    elif control_panel.get() == 2:
      EffectsFrame(self.panels_frame, data_vars)
    # --- DRAWING ---
    elif control_panel.get() == 3:
      DrawingFrame(self.panels_frame, data_vars, draw_color, draw_size)
    # --- DETECTION ---
    elif control_panel.get() == 4:
      DetectionFrame(self.panels_frame, data_vars)

  # --- animation ---
  def animate(self):
    if self.show_sidebar.get(): 
      self.animate_forward()
    else:
      self.animate_backward()

  def animate_forward(self):
    self.pos = (self.width * -1)
    self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1, anchor='nw')

  def animate_backward(self):
    self.pos = self.start_point
    self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1, anchor='nw')

# ---- Position Frame ---
class PositionFrame(ctk.CTkFrame):
  def __init__(self, parent, data_vars):
    super().__init__(master=parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    MEDIUM_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)
    ctk.CTkLabel(self, text='* TRANSFORMATION *', text_color=MAIN_COLOR, font=MEDIUM_FONT).pack(pady=10)

    # panels
    SliderPanel(self, 'Rotation', data_vars['rotate'][0], 0, 360)
    EntryPanel(self, 'Scaling', data_vars['scale_x'][0], data_vars['scale_y'][0])
    SegmentedPanel(self, 'Flipping', data_vars['flip'][0], FLIP_OPTIONS)
    SegmentedPanel(self, 'Cropping', data_vars['crop'][0], CROP_OPTIONS)


# ---- Colors Frame ---
class ColorsFrame(ctk.CTkFrame):
  def __init__(self, parent, data_vars):
    super().__init__(master=parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    MEDIUM_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)
    ctk.CTkLabel(self, text='* COLORS *', text_color=MAIN_COLOR, font=MEDIUM_FONT).pack(pady=10)
    
    # panels
    DropDownPanel(self, "Convert Colors", data_vars['convert'][0], CONVERT_OPTIONS)
    SliderPanel(self, 'Brightness', data_vars['brightness'][0], -100, 100)
    SliderPanel(self, 'Vibrance', data_vars['vibrance'][0], 0, 2)


# ---- Effects Frame ---
class EffectsFrame(ctk.CTkFrame):
  def __init__(self, parent, data_vars):
    super().__init__(master=parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    MEDIUM_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)
    ctk.CTkLabel(self, text='* EFFECTS *', text_color=MAIN_COLOR, font=MEDIUM_FONT).pack(pady=10)
    
    # panels
    SliderPanel(self, 'Blur', data_vars['blur'][0], 0, 100)
    SliderPanel(self, 'Sharping', data_vars['sharping'][0], 0, 5)
    MinMaxSliderPanel(self, 'Gray Level Slicing', (data_vars['gray_level_slicing_min'][0],data_vars['gray_level_slicing_max'][0]), (0,0), (255,255))
    SliderPanel(self, 'Bit Plane Slicing', data_vars['bit_plane_slicing'][0], 0, 7)
    SaltAndPapperPanel(self, 'Salt & Papper Noise', data_vars['s&p'][0], data_vars['median_blur'][0], data_vars['median_kernel'][0])
    DropDownPanel(self, "Filters", data_vars['filters'][0], FILTERS_OPTIONS)


# ---- Drawing Frame ---
class DrawingFrame(ctk.CTkFrame):
  def __init__(self, parent, data_vars, draw_color, draw_size):
    super().__init__(master=parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    MEDIUM_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)
    ctk.CTkLabel(self, text='* DRAWING *', text_color=MAIN_COLOR, font=MEDIUM_FONT).pack(pady=10)
    
    # panels
    DrawPanel(self, data_vars['draw'][0], DRAW_OPTIONS, draw_color, draw_size)
    TextPanel(self, 'Add Text', data_vars['text'][0])


# ---- Detection Frame ---
class DetectionFrame(ctk.CTkFrame):
  def __init__(self, parent, data_vars):
    super().__init__(master=parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    MEDIUM_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)
    ctk.CTkLabel(self, text='* DETECTION *', text_color=MAIN_COLOR, font=MEDIUM_FONT).pack(pady=10)
    
    # panels
    DetectionPanel(self, 'Detect Objects', data_vars['object_detection'][0])
