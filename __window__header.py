import customtkinter as ctk
from __settings import *
from __functions import *
from tkinter import filedialog

class WindowHeader(ctk.CTkFrame):
  def __init__(self, parent, show_sidebar, is_image, image_extension, import_fun, export_fun, edit_flag, undo_func, save_func):

    # setup
    super().__init__(master=parent, fg_color=SIDEBAR_COLOR, corner_radius=0)
    self.place(relx=0, rely=0, relwidth=1, relheight=0.07)
    self.is_image = is_image
    self.image_extension = image_extension
    self.show_sidebar = show_sidebar
    self.import_fun = import_fun
    self.export_fun = export_fun
    self.edit_flag = edit_flag
    self.undo_func = undo_func
    self.save_func = save_func


    # widgets
    if is_image.get(): 
    # --- Image Choosed ----
      # expand button 
      expand_icon = image_icon(EXPAND_IMAGE['light-dark'])
      expand_icon_colored = image_colored_icon(EXPAND_IMAGE['colored'])
      def on_enter(event):
        expand_button.configure(image=expand_icon_colored)
      def on_leave(event):
        expand_button.configure(image=expand_icon)
      expand_button = ctk.CTkButton(
        master=self,
        text='',
        fg_color=SIDEBAR_COLOR,
        hover_color=SIDEBAR_COLOR,
        image=expand_icon,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=lambda: self.show_sidebar.set(False if self.show_sidebar.get() else True))
      expand_button.pack(side='left', padx=10)
      expand_button.bind('<Enter>', on_enter, add='+')
      expand_button.bind("<Leave>", on_leave, add='+')

      # undo button 
      undo_icon = image_icon(UNDO_IMAGE['light-dark'])
      undo_icon_colored = image_colored_icon(UNDO_IMAGE['colored'])
      def on_enter(event):
        self.undo_button.configure(image=undo_icon_colored)
      def on_leave(event):
        self.undo_button.configure(image=undo_icon)
      self.undo_button = ctk.CTkButton(
        master=self,
        text='',
        fg_color=SIDEBAR_COLOR,
        hover_color=SIDEBAR_COLOR,
        image=undo_icon,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=self.undo_func)
      self.undo_button.bind('<Enter>', on_enter, add='+')
      self.undo_button.bind("<Leave>", on_leave, add='+')

      # save button 
      save_icon = image_icon(SAVE_IMAGE['light-dark'])
      save_icon_colored = image_colored_icon(SAVE_IMAGE['colored'])
      def on_save_enter(event):
        self.save_button.configure(image=save_icon_colored)
      def on_save_leave(event):
        self.save_button.configure(image=save_icon)
      self.save_button = ctk.CTkButton(
        master=self,
        text='',
        fg_color=SIDEBAR_COLOR,
        hover_color=SIDEBAR_COLOR,
        image=save_icon,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=self.save_func)
      self.save_button.bind('<Enter>', on_save_enter, add='+')
      self.save_button.bind("<Leave>", on_save_leave, add='+')

      # export button 
      export_icon = image_icon(EXPORT_IMAGE['light-dark'])
      export_icon_colored = image_colored_icon(EXPORT_IMAGE['colored'])
      def on_enter(event):
        export_button.configure(image=export_icon_colored, text_color=MAIN_COLOR)
      def on_leave(event):
        export_button.configure(image=export_icon, text_color=DARK)
      export_button = ctk.CTkButton(
        master=self,
        text='Save Image',
        fg_color=SIDEBAR_COLOR,
        text_color=DARK,
        image=export_icon,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=self.open_export_dialog)
      export_button.pack(side='left', padx=10)
      export_button.bind('<Enter>', on_enter, add='+')
      export_button.bind("<Leave>", on_leave, add='+')

      # close button
      close_button = ctk.CTkButton(
        master=self,
        text='X',
        fg_color='transparent',
        hover_color=RED_COLOR,
        border_width=2,
        text_color=DARK,
        border_color=RED_COLOR,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=lambda: self.is_image.set(False))
      close_button.pack(side='right', padx=10)

    else: 
    # --- No Image Choosed ----
      # import button
      icon = image_icon(IMPORT_IMAGE['light-dark'])
      icon_colored = image_colored_icon(IMPORT_IMAGE['colored'])
      def on_enter(event):
        import_button.configure(image=icon_colored)

      def on_leave(event):
        import_button.configure(image=icon)

      import_button = ctk.CTkButton(
        master=self,
        text='',
        fg_color=SIDEBAR_COLOR,
        hover_color=SIDEBAR_COLOR,
        image=icon,
        corner_radius=0,
        border_spacing=10,
        width=40,
        height=40,
        command=self.open_import_dialog)
      import_button.pack(side='right', padx=10)
      
      import_button.bind('<Enter>', on_enter, add='+')
      import_button.bind("<Leave>", on_leave, add='+')

      #  label
      ctk.CTkLabel(self, text='No Image Choosed', text_color=DARK).pack(side='left', padx=10)

  def open_import_dialog(self):
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path: self.import_fun(path)

  def open_export_dialog(self):
    file_path = filedialog.asksaveasfilename(title="Save Image", initialfile="donwload", defaultextension=self.image_extension, filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path: self.export_fun(file_path)

  def show_hide_undo(self, *args):
    if self.edit_flag.get():
      self.save_button.pack(side='left', padx=10)
      self.undo_button.pack(side='left', padx=10)
    else:
      self.save_button.pack_forget()
      self.undo_button.pack_forget()

