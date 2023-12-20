import customtkinter as ctk
from __settings import *
from __functions import *

class Sidebar(ctk.CTkFrame):
  def __init__(self, master, relx, relwidth, show_sidebar, control_panel, theme):

    # setup
    super().__init__(master=master, fg_color=SIDEBAR_COLOR,  corner_radius=0)
    self.control_panel = control_panel
    self.theme = theme

    # animation logic
    self.show_sidebar = show_sidebar
    self.start_point = relx
    self.width = relwidth
    self.pos = relx

    # layout
    self.place(relx=self.start_point, rely=0, relwidth=self.width, relheight=1, anchor='nw')

    # some space
    ctk.CTkLabel(self, text='', fg_color=SIDEBAR_COLOR, corner_radius=0, height=70).pack(fill='x')

    # buttons
    self.position_button = SidebarButton(self, 0, self.switch_button)
    self.colors_button = SidebarButton(self, 1, self.switch_button)
    self.effects_button = SidebarButton(self, 2, self.switch_button)
    self.drawing_button = SidebarButton(self, 3, self.switch_button)
    self.detection_button = SidebarButton(self, 4, self.switch_button)
    self.set_active(0)

    # theme toggoler
    icon = image_icon(THEME_TOGGOLER_IMAGE['light-dark'])
    icon_colored = image_icon(THEME_TOGGOLER_IMAGE['colored'])
    def on_enter(event):
      theme_togoler.configure(image=icon_colored)

    def on_leave(event):
      theme_togoler.configure(image=icon)

    theme_togoler = ctk.CTkButton(
    master=self,
    text='',
    fg_color=SIDEBAR_COLOR,
    hover_color=SIDEBAR_COLOR,
    image=icon,
    corner_radius=0,
    border_spacing=10,
    height=100,
    command=lambda: self.theme.set("light" if self.theme.get() == 'dark' else "dark")
    )
    theme_togoler.pack(fill='x', side='bottom')
    
    theme_togoler.bind('<Enter>', on_enter, add='+')
    theme_togoler.bind("<Leave>", on_leave, add='+')


  # switch buttons
  def switch_button(self, index):
    self.control_panel.set(index)
    self.set_active(index)

  def set_active(self, index):
    self.position_button.configure(fg_color=SIDEBAR_COLOR, image=image_icon(SIDEBAR_BUTTONS[0]['images']['light-dark']))
    self.colors_button.configure(fg_color=SIDEBAR_COLOR, image=image_icon(SIDEBAR_BUTTONS[1]['images']['light-dark']))
    self.effects_button.configure(fg_color=SIDEBAR_COLOR, image=image_icon(SIDEBAR_BUTTONS[2]['images']['light-dark']))
    self.drawing_button.configure(fg_color=SIDEBAR_COLOR, image=image_icon(SIDEBAR_BUTTONS[3]['images']['light-dark']))
    self.detection_button.configure(fg_color=SIDEBAR_COLOR, image=image_icon(SIDEBAR_BUTTONS[4]['images']['light-dark']))

    if index == 0: 
      self.position_button.configure(
        fg_color=CONTROL_COLOR, 
        image=ctk.CTkImage(light_image=Image.open(SIDEBAR_BUTTONS[0]['images']['colored']), 
        size=(24, 24)))
    elif index == 1: 
      self.colors_button.configure(
        fg_color=CONTROL_COLOR, 
        image=ctk.CTkImage(light_image=Image.open(SIDEBAR_BUTTONS[1]['images']['colored']), 
        size=(24, 24)))
    elif index == 2: 
      self.effects_button.configure(
        fg_color=CONTROL_COLOR, 
        image=ctk.CTkImage(light_image=Image.open(SIDEBAR_BUTTONS[2]['images']['colored']), 
        size=(24, 24)))
    elif index == 3: 
      self.drawing_button.configure(
        fg_color=CONTROL_COLOR, 
        image=ctk.CTkImage(light_image=Image.open(SIDEBAR_BUTTONS[3]['images']['colored']), 
        size=(24, 24)))
    elif index == 4: 
      self.detection_button.configure(
        fg_color=CONTROL_COLOR, 
        image=ctk.CTkImage(light_image=Image.open(SIDEBAR_BUTTONS[4]['images']['colored']), 
        size=(24, 24)))

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



class SidebarButton(ctk.CTkButton):
  def __init__(self, master, index, switch_func, fg_color=SIDEBAR_COLOR):
    icon = image_icon(SIDEBAR_BUTTONS[index]['images']['light-dark'])
    super().__init__(
    master=master,
    text='',
    fg_color=fg_color,
    hover_color=CONTROL_COLOR,
    image=icon,
    corner_radius=2,
    border_spacing=5,
    height=80,
    command=lambda: switch_func(index)
    )
    self.pack(fill='x', padx=(10, 0))