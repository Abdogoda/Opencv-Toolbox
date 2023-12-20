import customtkinter as ctk
from __settings import *
from __functions import *
from CTkColorPicker import *

class Panel(ctk.CTkFrame):
 def __init__(self, master):
  super().__init__(master=master, fg_color=SIDEBAR_COLOR, corner_radius=5)
  self.pack(fill='x', pady=4, ipady=8)


class SliderPanel(Panel):
  def __init__(self, master, text, data_var, min_value, max_value):
    super().__init__(master=master)
    self.rowconfigure((0,1), weight=1, uniform='a')
    self.columnconfigure((0,1), weight=1, uniform='a')
    self.data_var = data_var
    self.data_var.trace('w', self.update_label)
    self.label_var = ctk.StringVar(value='0.0')

    ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky='w', padx=8)
    self.num_label = ctk.CTkLabel(self, text='0.0', textvariable=self.label_var)
    self.num_label.grid(column=1, row=0, sticky='e', padx=8)
    ctk.CTkSlider(
      self, 
      variable=self.data_var, 
      from_=min_value,
      to=max_value, 
      fg_color=BACKGOUND_COLOR,
      button_color=MAIN_COLOR,
      button_hover_color=SECOND_COLOR,
      command=self.update_label).grid(column=0, row=1, columnspan=2, sticky='ew', padx=8, pady=8)
    self.update_label()

  def update_label(self, *args):
    self.label_var.set(f"{round(float(self.data_var.get()), 2)}")

class MinMaxSliderPanel(Panel):
  def __init__(self, master, text, data_var, min_value, max_value):
    super().__init__(master=master)
    self.rowconfigure((0,1,2), weight=1, uniform='a')
    self.columnconfigure((0,1), weight=1, uniform='a')
    self.data_var_min = data_var[0]
    self.data_var_max = data_var[1]
    self.data_var_min.trace('w', self.update_label_min)
    self.data_var_max.trace('w', self.update_label_max)
    self.label_var_min = ctk.StringVar(value='Min: 0')
    self.label_var_max = ctk.StringVar(value='Max: 0')

    ctk.CTkLabel(self, text=text).grid(column=0, row=0, columnspan=2, sticky='w', padx=8)
    self.num_label_min = ctk.CTkLabel(self, text='Min: 0', textvariable=self.label_var_min)
    self.num_label_min.grid(column=0, row=1, sticky='w', padx=8)
    self.num_label_max = ctk.CTkLabel(self, text='Max: 0', textvariable=self.label_var_max)
    self.num_label_max.grid(column=1, row=1, sticky='e', padx=8)

    ctk.CTkSlider(
      self, 
      variable=self.data_var_min, 
      from_=min_value[0],
      to=max_value[0], 
      fg_color=BACKGOUND_COLOR,
      button_color=MAIN_COLOR,
      button_hover_color=SECOND_COLOR,
      command=self.update_label_min).grid(column=0, row=2, sticky='ew', padx=4, pady=6)
    ctk.CTkSlider(
      self, 
      variable=self.data_var_max, 
      from_=min_value[1],
      to=max_value[1], 
      fg_color=BACKGOUND_COLOR,
      button_color=MAIN_COLOR,
      button_hover_color=SECOND_COLOR,
      command=self.update_label_max).grid(column=1, row=2, sticky='ew', padx=4, pady=6)

    self.update_label_min()
    self.update_label_max()

  def update_label_min(self, *args):
    self.label_var_min.set(f"Min: {int(self.data_var_min.get())}")
  def update_label_max(self, *args):
    self.label_var_max.set(f"Max: {int(self.data_var_max.get())}")


class SegmentedPanel(Panel):
  def __init__(self, master, text, data_var, options):
    super().__init__(master=master)
    self.rowconfigure((0,1), weight=1, uniform='a')
    self.columnconfigure((0,1), weight=1, uniform='a')

    ctk.CTkLabel(self, text=text, anchor='w').pack(expand=True, fill='x', padx=8)
    ctk.CTkSegmentedButton(self, 
    values=options, 
    variable=data_var, 
    selected_color=MAIN_COLOR, 
    selected_hover_color=SECOND_COLOR, 
    text_color=DARK).pack(expand=True, fill='both', padx=5, pady=5)


class EntryPanel(Panel):
  def __init__(self, master, text, data_var_1, data_var_2):
    super().__init__(master=master)
    self.rowconfigure((0,1), weight=1, uniform='a')
    self.columnconfigure((0,2), weight=1, uniform='a')
    self.columnconfigure((1,3), weight=4, uniform='a')
    
    self.data_var_1 = data_var_1
    self.data_var_2 = data_var_2
    self.data_var_1.trace('w', self.update_entry_label)
    self.data_var_2.trace('w', self.update_entry_label)
    self.entry_label_var = ctk.StringVar(value='1.0 : 1.0')

    ctk.CTkLabel(master=self, text=text).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    ctk.CTkLabel(master=self, textvariable=self.entry_label_var).grid(row=0, column=3, padx=5, pady=5, sticky='e')

    ctk.CTkLabel(master=self, text='X:').grid(row=1, column=0, pady=5)
    ctk.CTkEntry(master=self, placeholder_text='Scale X', placeholder_text_color=MAIN_COLOR, textvariable=self.data_var_1).grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(master=self, text='Y:').grid(row=1, column=2, pady=5)
    ctk.CTkEntry(master=self, placeholder_text='Scale Y', placeholder_text_color=MAIN_COLOR, textvariable=self.data_var_2).grid(row=1, column=3, padx=5, pady=5)

  def update_entry_label(self, *args):
    self.entry_label_var.set(f"{round(self.data_var_1.get(), 2), round(self.data_var_2.get(), 2)}")



class SaltAndPapperPanel(Panel):
  def __init__(self, master, text, salt_papper_var, median_var, kernel_var):
    super().__init__(master=master)
    ctk.CTkLabel(self, text=text, anchor='w').pack(fill='x' ,expand=True, padx=5, pady=5)

    frame1 = ctk.CTkFrame(self)
    frame1.pack(expand=True, fill='x', padx=5, pady=5)

    ctk.CTkSwitch(
      frame1, 
      text='Add S&P Noise', 
      variable=salt_papper_var, 
      button_color=MAIN_COLOR, 
      button_hover_color=SECOND_COLOR, 
      fg_color=BACKGOUND_COLOR,
      progress_color=DARK).pack(side='left', expand=True, padx=5, pady=5, anchor='w')

    frame2 = ctk.CTkFrame(self)
    frame2.pack(expand=True, fill='x', padx=5, pady=5)

    ctk.CTkLabel(frame2, text='Ksize:').pack(side='left', expand=True, fill='x', padx=5, pady=5)
    ctk.CTkEntry(master=frame2, placeholder_text='Ksize', textvariable=kernel_var, width=50).pack(side='left', expand=True, padx=5, pady=5)
    ctk.CTkButton(master=frame2, text='Remove S&P',fg_color=MAIN_COLOR, hover_color=SECOND_COLOR, text_color=LIGHT, command=lambda: median_var.set(False if median_var.get() else True)).pack(side='left', expand=True, padx=5, pady=5)


class DropDownPanel(Panel):
  def __init__(self, master, text, data_var, options):
    super().__init__(master=master)
    ctk.CTkLabel(self, text=text, anchor='w').pack(expand=True, fill='x', padx=8)
    ctk.CTkOptionMenu(master=self, 
      values=options, 
      fg_color=BACKGOUND_COLOR,
      button_color=MAIN_COLOR,
      button_hover_color=SECOND_COLOR,
      dropdown_fg_color=CONTROL_COLOR,
      text_color=DARK,
      variable=data_var).pack(fill='x', pady=4, padx=8)


class DrawPanel(Panel):
  def __init__(self, master, data_var, options, draw_color, draw_size):
    super().__init__(master=master)
    self.rowconfigure((0,1,2,3), weight=1, uniform='r')
    self.columnconfigure((0,1,2), weight=1, uniform='c')

    self.size_var = draw_size
    self.color_var = draw_color

    # size
    ctk.CTkLabel(self, text='Size').grid(row=0, column=0, sticky='w', padx=8)
    ctk.CTkLabel(self, text='1', textvariable=self.size_var).grid(row=0, column=2, sticky='e', padx=8)
    ctk.CTkSlider(
      self, 
      variable=self.size_var, 
      from_=1,
      to=128, 
      fg_color=BACKGOUND_COLOR,
      button_color=MAIN_COLOR,
      button_hover_color=SECOND_COLOR).grid(row=1, column=0, columnspan=3, sticky='we', padx=8, pady=(0, 5))

    # color
    picker_color_icon = image_colored_icon(COLOR_PICKER_IMAGE)
    self.color_picker = ctk.CTkButton(
      self, 
      text="Pick Color", 
      compound='left', 
      image=picker_color_icon, 
      fg_color='transparent', 
      anchor="w", 
      hover_color=SIDEBAR_COLOR, 
      text_color=DARK, 
      command=self.ask_color)
    self.color_picker.grid(row=2, column=0, columnspan=2, sticky='w', pady=5, padx=8)
    self.color_label = ctk.CTkLabel(self, textvariable=self.color_var, text_color=DARK)
    self.color_label.grid(row=2, column=2, sticky='e', pady=5, padx=8)

    # draw option
    ctk.CTkSegmentedButton(self, 
    values=options, 
    variable=data_var, 
    selected_color=MAIN_COLOR, 
    selected_hover_color=SECOND_COLOR, 
    text_color=DARK).grid(row=3, column=0, columnspan=3, sticky='we', pady=8, padx=8)


  def ask_color(self):
    pick_color = AskColor() # open the color picker
    color = pick_color.get() # get the color string
    self.color_label.configure(text_color=color)
    self.color_var.set(color)


class TextPanel(Panel):
  def __init__(self, master, text, data_var):
    super().__init__(master=master)
    self.rowconfigure((0,1), weight=1, uniform='r')
    self.columnconfigure(0, weight=1, uniform='c')

    self.data_var = data_var

    ctk.CTkLabel(self, text=text).grid(row=0, column=0, sticky='w', padx=8)
    ctk.CTkEntry(
      self, 
      textvariable=self.data_var, 
      ).grid(row=1, column=0, sticky='we', padx=8, pady=5)


class DetectionPanel(Panel):
  def __init__(self, master, text, data_var):
    super().__init__(master=master)
    self.rowconfigure((0,1), weight=1, uniform='r')
    self.columnconfigure(0, weight=1, uniform='c')

    self.data_var = data_var

    ctk.CTkButton(
    master=self, 
    text=text,
    command=lambda: data_var.set(True),
    fg_color=MAIN_COLOR, 
    text_color=LIGHT, 
    corner_radius=5, 
    hover_color=SECOND_COLOR).pack(pady=10)

