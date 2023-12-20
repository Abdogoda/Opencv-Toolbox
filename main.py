import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import numpy as np
from datetime import datetime
import os
from __settings import *
from __functions import *
from __preloader import *
from __main__window import *
from __sidebar import *
from __controlbar import *
from __message import *
from detection_function import image_detection


class Main(ctk.CTk):
  def __init__(self):

    # setup
    super().__init__()
    self.geometry('1200x700')
    self.minsize(1000, 600)
    self.title('Photo Editor')
    self.iconbitmap('images/favicon.ico')

    # data
    MAIN_FONT = ctk.CTkFont(family=FONT_FAMILY, size=SMALL_FONT_SIZE)
    STYLED_FONT = ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE)

    # flags
    self.CROP_FLAG = False
    self.DRAW_FLAG = False
    self.TEXT_FLAG = False

    # canvas data
    self.image_width = 0
    self.image_height = 0
    self.canvas_width = 0
    self.canvas_height = 0
    self.image_ratio = 0

    # importnant functions
    self.init_program()
    self.show_window()

    # preloader
    # def switch_to_app_frame():
    #   self.preloader.destroy()
    #   self.show_window()
    # self.preloader = Preloader(master=self, callback=switch_to_app_frame)


    # run the program 
    ctk.set_appearance_mode(self.THEME.get())
    self.mainloop()

  # ---- Show Editor ----- 
  def show_window(self):
    self.main_window = Window(master=self, 
      relx=0, 
      relwidth=1, 
      show_sidebar=self.SHOW_SIDEBAR, 
      is_image=self.IS_IMAGE, 
      image_extension=self.image_extension,
      import_fun=self.import_image, 
      resize_image = self.resize_image, 
      export_fun=self.export_image, 
      crop_var=self.data_vars['crop'][0], crop_func=self.crop_func,
      draw_var=self.data_vars['draw'][0], draw_func=self.draw_func, 
      text_var=self.data_vars['text'][0], text_func=self.text_func,
      draw_size=self.draw_size, 
      draw_color=self.draw_color,
      edit_flag=self.EDIT_FLAG, 
      undo_func=self.undo_func,
      save_func=self.save_func)

  # ---- Show Editor Windows ----- 
  def show_editor(self):
    self.main_window.destroy()
    self.sidebar = Sidebar(master=self, 
      relx=0, relwidth=0.05, show_sidebar=self.SHOW_SIDEBAR, 
      control_panel=self.CONTROL_PANEL, theme=self.THEME)

    self.controlbar = Controlbar(master=self, 
      relx=0.05, relwidth=0.20, show_sidebar=self.SHOW_SIDEBAR, control_panel=self.CONTROL_PANEL,
      data_vars=self.data_vars, draw_color=self.draw_color, draw_size=self.draw_size)

    self.main_window = Window(master=self, 
      relx=0.25, 
      relwidth=0.75, 
      show_sidebar=self.SHOW_SIDEBAR, 
      is_image=self.IS_IMAGE, 
      image_extension=self.image_extension,
      import_fun=self.import_image, 
      resize_image = self.resize_image, 
      export_fun = self.export_image, 
      crop_var=self.data_vars['crop'][0], crop_func=self.crop_func,
      draw_var=self.data_vars['draw'][0], draw_func=self.draw_func, 
      text_var=self.data_vars['text'][0], text_func=self.text_func,
      draw_size=self.draw_size,
      draw_color=self.draw_color,
      edit_flag=self.EDIT_FLAG, 
      undo_func=self.undo_func,
      save_func=self.save_func)

  # ---- Switch Theme ----- 
  def switch_theme(self, *args):
    ctk.set_appearance_mode(self.THEME.get())

  # ---- Switch Panels ----- 
  def switch_panels(self, *args):
    self.controlbar.destroy()
    self.controlbar = Controlbar(master=self, relx=0.05, relwidth=0.20, show_sidebar=self.SHOW_SIDEBAR, control_panel=self.CONTROL_PANEL,
    data_vars=self.data_vars, draw_color=self.draw_color, draw_size=self.draw_size)

  # ---- Switch Show Sidebar ----- 
  def switch_show_sidebar(self, *args):
    self.sidebar.animate()
    self.controlbar.animate()
    self.main_window.animate()

# ---- Resize & Place Image Function ---
  def resize_image(self, event):
    canvas_ratio = event.width / event.height
    self.canvas_width = event.width
    self.canvas_height = event.height

    bigger_width = self.canvas_width
    bigger_height = self.canvas_height
    if self.image is not None:
      if self.image_width > self.canvas_width: bigger_width = self.image_width
      if self.image_height > self.canvas_height: bigger_height = self.image_height

    self.main_window.draw_grid(bigger_width, bigger_height)

    if self.IS_IMAGE.get():
      self.display_image()

  # ---- Import Image ----- 
  def import_image(self, image_path):
    _, self.image_extension = os.path.splitext(image_path)
    self.image_extension = self.image_extension.lower() 
    self.original = cv2.imread(image_path)
    self.image = self.original
    self.image_width = self.image.shape[1]
    self.image_height = self.image.shape[0]
    self.IS_IMAGE.set(True)
    self.display_image()

  # ---- Export Image ----- 
  def export_image(self, path):
    if self.image is not None:
      cv2.imwrite(path, self.image)
      success_box = CustomSuccessMessageBox(master=self, text="Image Saved Successfully!", type="success")

  # ---- Switch Is Image ----- 
  def switch_is_image(self, *args):
    if self.IS_IMAGE.get():
      self.show_editor()
    else:
      self.image = None
      self.reset_changes()
      self.show_window()

  # ---- Reset Changes ----- 
  def reset_changes(self):
    for key, value in self.data_vars.items():
      value[0].set(value[1]) 
    self.CROP_FLAG = False
    self.DRAW_FLAG = False
    self.TEXT_FLAG = False
    self.image_extension = '.png'
    self.crop_data = []
    self.draw_data = []
    self.image_changes = []
    self.EDIT_FLAG.set(False)

  # ---- Display Image ----
  def display_image(self):
    if self.image is not None and self.image_width > 0 and self.image_height > 0:
      image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
      pil_image = Image.fromarray(image_rgb)
      tk_image = ImageTk.PhotoImage(pil_image)

      self.main_window.show_image(tk_image=tk_image, img_dimns=(self.image_width,self.image_height))

  # ----- Init Program -----
  def init_program(self):
    self.CONTROL_PANEL = ctk.IntVar(value=0)
    self.CONTROL_PANEL.trace('w', self.switch_panels)

    self.THEME = ctk.StringVar(value='dark')
    self.THEME.trace('w', self.switch_theme)

    self.sidebar = False
    self.controlbar = False

    self.SHOW_SIDEBAR = ctk.BooleanVar(value=False)
    self.SHOW_SIDEBAR.trace('w', self.switch_show_sidebar)

    self.IS_IMAGE = ctk.BooleanVar(value=False)
    self.IS_IMAGE.trace('w', self.switch_is_image)

    self.image_extension = '.png'
    self.image = None

    self.image_changes = []
    self.EDIT_FLAG = ctk.BooleanVar(value=False)
    self.EDIT_FLAG.trace('w', self.show_hide_undo)

    self.data_vars = {
      'rotate' : [ctk.IntVar(value=ROTATE_DEFAULT), ROTATE_DEFAULT],
      'scale_x' : [ctk.DoubleVar(value=SCALE_FACTOR_X), SCALE_FACTOR_X],
      'scale_y' : [ctk.DoubleVar(value=SCALE_FACTOR_Y), SCALE_FACTOR_Y],
      'flip' : [ctk.StringVar(value=FLIP_OPTIONS[0]), FLIP_OPTIONS[0]],
      'crop' : [ctk.StringVar(value=CROP_OPTIONS[0]), CROP_OPTIONS[0]],

      'brightness' : [ctk.DoubleVar(value=BRIGHTNESS_DEFAULT), BRIGHTNESS_DEFAULT] ,
      'grayscale' : [ctk.BooleanVar(value=GRAYSCALE_DEFAULT), GRAYSCALE_DEFAULT] ,
      'convert' : [ctk.StringVar(value=CONVERT_OPTIONS[0]), CONVERT_OPTIONS[0]] ,
      'vibrance' : [ctk.DoubleVar(value=VIBRANCE_DEFAULT), VIBRANCE_DEFAULT] ,
      
      'blur' : [ctk.DoubleVar(value=BLUR_DEFAULT), BLUR_DEFAULT],
      'sharping' : [ctk.IntVar(value=SHARPING_DEFAULT), SHARPING_DEFAULT],
      'gray_level_slicing_min' : [ctk.IntVar(value=GRAY_LEVEL_SLICING_MIN_DEFUALT), GRAY_LEVEL_SLICING_MIN_DEFUALT],
      'gray_level_slicing_max' : [ctk.IntVar(value=GRAY_LEVEL_SLICING_MAX_DEFUALT), GRAY_LEVEL_SLICING_MAX_DEFUALT],
      'bit_plane_slicing' : [ctk.IntVar(value=BIT_PLANE_SLICING_DEFUALT), BIT_PLANE_SLICING_DEFUALT],
      'filters' : [ctk.StringVar(value=FILTERS_OPTIONS[0]), FILTERS_OPTIONS[0]],
      's&p' : [ctk.BooleanVar(value=SALT_PAPPER_DEFAULT), SALT_PAPPER_DEFAULT],
      'median_blur' : [ctk.BooleanVar(value=MEDIAN_BLUR_DEFAULT), MEDIAN_BLUR_DEFAULT],
      'median_kernel' : [ctk.IntVar(value=MEDIAN_KERNEL_DEFAULT), MEDIAN_KERNEL_DEFAULT],
      
      'draw' : [ctk.StringVar(value=DRAW_OPTIONS[0]), DRAW_OPTIONS[0]],
      'text' : [ctk.StringVar(value=''), ''],

      'object_detection' : [ctk.BooleanVar(value=False), False]
    }
    self.draw_size = ctk.IntVar(value=1)
    self.draw_color = ctk.StringVar(value="#000000")

    # tracing the variables
    for key, value in self.data_vars.items():
      value[0].trace('w', self.editing_image)

  # ---- Crop Function ----
  def crop_func(self, crop_data):
    self.CROP_FLAG = False
    if self.data_vars['crop'][0].get() != CROP_OPTIONS[0]:
      if len(crop_data) > 0:
        self.CROP_FLAG = True
        self.crop_data = crop_data
      self.editing_image(str(self.data_vars['crop'][0]))

  # ---- draw Function ----
  def draw_func(self, draw_data):
    self.DRAW_FLAG = False
    if self.data_vars['draw'][0].get() != DRAW_OPTIONS[0]:
      if len(draw_data) > 0:
        if self.data_vars['draw'][0].get() != 'Fill':
          self.FILL_FLAG = False
          self.DRAW_FLAG = True
          self.draw_data.append(draw_data) 
    else:
        self.draw_data = []
    self.editing_image(str(self.data_vars['draw'][0]))

  # ---- text Function ----
  def text_func(self, position):
    self.TEXT_FLAG = False
    if self.data_vars['draw'][0].get() != '':
      self.TEXT_FLAG = True
      self.text_position = position
    self.editing_image(str(self.data_vars['text'][0]))

  # ----- Editing The Image -----
  def editing_image(self, *args):
    self.image = self.original.copy()
    self.EDIT_FLAG.set(True)
    flag_status = 0

    # rotating the image
    if self.data_vars['rotate'][0].get() != ROTATE_DEFAULT:
      flag_status = 1
      center = (self.image.shape[1] // 2, self.image.shape[0] // 2)
      rotation_matrix = cv2.getRotationMatrix2D(center, self.data_vars['rotate'][0].get(), scale=1.0)
      self.image = cv2.warpAffine(self.image, rotation_matrix, (self.image.shape[1], self.image.shape[0]))

    # scale the image
    if self.data_vars['scale_x'][0].get() != SCALE_FACTOR_X or self.data_vars['scale_y'][0].get() != SCALE_FACTOR_Y :
      if isinstance(self.data_vars['scale_x'][0].get(), float) and isinstance(self.data_vars['scale_y'][0].get(), float) and self.data_vars['scale_x'][0].get() > 0 and self.data_vars['scale_y'][0].get() > 0:
        flag_status = 1
        self.image = cv2.resize(self.original, (0, 0), fx=self.data_vars['scale_x'][0].get(), fy=self.data_vars['scale_y'][0].get())

    # flip
    if self.data_vars['flip'][0].get() != FLIP_OPTIONS[0]:
      flag_status = 1
      flip_var = self.data_vars['flip'][0].get()
      if flip_var == 'X':
        self.image = cv2.flip(self.image, 1)
      elif flip_var == 'Y':
        self.image = cv2.flip(self.image, 0)
      elif flip_var == 'Both':
        self.image = cv2.flip(self.image, -1)

    # crop
    if self.data_vars['crop'][0].get() != CROP_OPTIONS[0] and self.CROP_FLAG:
      flag_status = 1
      start_x, start_y, end_x, end_y = int(self.crop_data['coordinates'][0][0]), int(self.crop_data['coordinates'][0][1]), int(self.crop_data['coordinates'][1][0]), int(self.crop_data['coordinates'][1][1])

      if self.crop_data['type'] == 'Rect':
        self.image = self.image[start_y:end_y, start_x:end_x]

      elif self.crop_data['type'] == 'Circle':
        center_x = (start_x + end_x) // 2
        center_y = (start_y + end_y) // 2
        radius = min(abs(end_x - start_x), abs(end_y - start_y)) // 2
        mask = np.zeros((self.image.shape[0], self.image.shape[1], self.image.shape[2]), dtype=np.uint8)
        cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), thickness=cv2.FILLED)
        self.image = cv2.bitwise_and(self.image, mask)

    # convert
    if self.data_vars['convert'][0].get() != CONVERT_OPTIONS[0]:
      flag_status = 1
      convert_var = self.data_vars['convert'][0].get()
      if convert_var == 'BGR to RGB':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
      elif convert_var == 'BGR to Grayscale':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
      elif convert_var == 'RGB to BGR':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
      elif convert_var == 'BGR to HSV':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
      elif convert_var == 'BGR to LAB':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
      elif convert_var == 'HSV to BGR':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)
      elif convert_var == 'Blue':
        b, g, r = cv2.split(self.image)
        blank = np.zeros(self.image.shape[:2], dtype="uint8")
        self.image = cv2.merge([b,blank,blank])
      elif convert_var == 'Green':
        b, g, r = cv2.split(self.image)
        blank = np.zeros(self.image.shape[:2], dtype="uint8")
        self.image = cv2.merge([blank,g,blank])
      elif convert_var == 'Red':
        b, g, r = cv2.split(self.image)
        blank = np.zeros(self.image.shape[:2], dtype="uint8")
        self.image = cv2.merge([blank,blank,r])

    # brightness
    if self.data_vars['brightness'][0].get() != BRIGHTNESS_DEFAULT:
      flag_status = 1
      img_float = self.image.astype(np.float32) / 255.0
      img_float = img_float + self.data_vars['brightness'][0].get() / 100.0
      img_float = np.clip(img_float, 0.0, 1.0)
      self.image = (img_float * 255).astype(np.uint8)

    # vibrance
    if self.data_vars['vibrance'][0].get() != BRIGHTNESS_DEFAULT:
      if self.data_vars['convert'][0].get() != 'BGR to Grayscale':
        flag_status = 1
        img_float = self.image.astype(np.float32) / 255.0
        vibrance = self.data_vars['vibrance'][0].get()
        vibrance_matrix = np.array([[1 + vibrance, 0, 0], [0, 1 + vibrance, 0], [0, 0, 1 + vibrance]])
        img_float = cv2.transform(img_float, vibrance_matrix)
        img_float = np.clip(img_float, 0.0, 1.0)
        self.image = (img_float * 255).astype(np.uint8)

    # blur
    if self.data_vars['blur'][0].get() != BLUR_DEFAULT:
      flag_status = 1
      self.image = cv2.GaussianBlur(self.image, (2 * int(self.data_vars['blur'][0].get()) + 1, 2 * int(self.data_vars['blur'][0].get()) + 1), 0)

    # sharping
    if self.data_vars['sharping'][0].get() != SHARPING_DEFAULT:
      flag_status = 1
      blurred = cv2.GaussianBlur(self.image, (0, 0), self.data_vars['sharping'][0].get())
      strength = 2.0 * self.data_vars['sharping'][0].get()
      mask = cv2.addWeighted(self.image, 1 + strength, blurred, -strength, 0)
      mask = np.clip(mask, 0, 255)
      self.image = mask.astype(np.uint8)

    # gray level slicing
    if self.data_vars['gray_level_slicing_min'][0].get() != GRAY_LEVEL_SLICING_MIN_DEFUALT or self.data_vars['gray_level_slicing_max'][0].get() != GRAY_LEVEL_SLICING_MAX_DEFUALT:
      if self.data_vars['bit_plane_slicing'][0].get() == BIT_PLANE_SLICING_DEFUALT:
        flag_status = 1
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(gray, self.data_vars['gray_level_slicing_min'][0].get(), self.data_vars['gray_level_slicing_max'][0].get())
        self.image = cv2.bitwise_and(gray, gray, mask=mask)

    # Bit plane slicing
    if self.data_vars['bit_plane_slicing'][0].get() != BIT_PLANE_SLICING_DEFUALT:
      if self.data_vars['gray_level_slicing_min'][0].get() == GRAY_LEVEL_SLICING_MIN_DEFUALT and self.data_vars['gray_level_slicing_max'][0].get() == GRAY_LEVEL_SLICING_MAX_DEFUALT:
        flag_status = 1
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        bit_plane = (gray >> self.data_vars['bit_plane_slicing'][0].get()) & 1
        self.image = bit_plane * 255

    # Salt And Papper Noise
    if self.data_vars['s&p'][0].get() != SALT_PAPPER_DEFAULT:
      if self.data_vars['s&p'][0].get():
        flag_status = 1
        # Specify probabilities for salt and pepper noise
        salt_prob = 0.01  # adjust as needed
        pepper_prob = 0.01  # adjust as needed

        # Add salt noise
        salt_mask = np.random.rand(*self.image.shape[:2]) < salt_prob
        self.image[salt_mask] = 255

        # Add pepper noise
        pepper_mask = np.random.rand(*self.image.shape[:2]) < pepper_prob
        self.image[pepper_mask] = 0

    # Mdeian Blur For Salt And Papper Noise
    if self.data_vars['median_blur'][0].get() != SALT_PAPPER_DEFAULT:
      if self.data_vars['median_blur'][0].get():
        if isinstance(self.data_vars['median_kernel'][0].get(), int) and self.data_vars['median_kernel'][0].get() > 0 and self.data_vars['median_kernel'][0].get() % 2 != 0:
          flag_status = 1
          
          self.image = cv2.medianBlur(self.image, self.data_vars['median_kernel'][0].get())
        else:
          self.data_vars['median_blur'][0].set(False)

    # filters
    if self.data_vars['filters'][0].get() != FILTERS_OPTIONS[0]:
      flag_status = 1
      used_filter = self.data_vars['filters'][0].get()
      gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
      rows, cols = gray.shape
      if used_filter == 'Emboss':
        kernel_emboss = np.array([[0, -1, -1],[1,  0, -1],[1,  1,  0]])
        self.image = cv2.filter2D(self.image, -1, kernel_emboss)
      elif used_filter == 'Find Edges':
        self.image = cv2.Canny(self.image, 100, 200)
      elif used_filter == 'Threshold':
        _, self.image = cv2.threshold(self.image, 128, 255, cv2.THRESH_BINARY)
      elif used_filter == 'Contour':
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image, contours, -1, (0, 255, 0), 2)
      elif used_filter == 'Filter2D':
        kernel = np.ones((3, 3), np.int8) / 9
        self.image = cv2.filter2D(self.image, cv2.CV_8UC1, kernel)
      elif used_filter == 'Histogram Equalization':
        self.image = cv2.equalizeHist(gray)
      elif used_filter == 'Logarithmic Transformation':
        l_t = 1 * np.log1p(gray)
        self.image = (255 * (l_t - np.min(l_t)) / (np.max(l_t) - np.min(l_t))).astype(np.uint8)
      elif used_filter == 'Power Transformation':
        p_t = np.power(gray, 0.5)
        self.image = (255 * (p_t - np.min(p_t)) / (np.max(p_t) - np.min(p_t))).astype(np.uint8)

    # draw
    if self.data_vars['draw'][0].get() != DRAW_OPTIONS[0]:
      flag_status = 1
      hex_color = self.draw_color.get().lstrip('#')
      color = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))
      if self.data_vars['draw'][0].get() == 'Fill':
        self.image[:,:] = color 
      elif self.data_vars['draw'][0].get() == 'Brush' and self.DRAW_FLAG:
        for lis in self.draw_data:
          for i in range(0, len(lis)-1):
            cv2.line(self.image, lis[i], lis[i+1], color, self.draw_size.get())
      else:
        self.DRAW_FLAG = False
        self.draw_data = []

    # text
    if self.data_vars['text'][0].get() != '' and self.TEXT_FLAG:
      flag_status = 1
      hex_color = self.draw_color.get().lstrip('#')
      color = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))
      cv2.putText(self.image, self.data_vars['text'][0].get(), self.text_position, cv2.FONT_HERSHEY_SIMPLEX, self.draw_size.get(), color, 2)

    # detection
    if self.data_vars['object_detection'][0].get() != False:
      image_detection(self.image)
      
      detected_image = [f for f in os.listdir('runs/predict') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))][0]
      if not detected_image:  return
      
      self.detected_image_path = 'runs/predict/' + detected_image
      self.pill_detected_image = Image.open(self.detected_image_path)
      size_x = self.image_width if self.image_width < 300 else 300
      size_y = self.image_height if self.image_height < 300 else 300
      self.detected_image = ctk.CTkImage(self.pill_detected_image, size=(size_x, size_y))
        
      self.data_vars['object_detection'][0].set(False)
      TopLevelDetection(master=self, image=self.detected_image, save_func=self.save_detected_image)

    # add to changes list
    if len(args) > 0:
      for key, value in self.data_vars.items():
        if str(args[0]) == str(value[0]):
          self.replace_changes(key)

    # if there are no changes ==> unpick undo button
    if flag_status == 0:
      self.EDIT_FLAG.set(False)

    # reset windows
    self.main_window.destroy_all()
    self.main_window.draw_grid(2000, 1000)
    self.display_image()

  # ---- Canvas To Image Coordinates ----
  def canvas_to_image_coordinates(self, point):
    x_resized = point[0] / self.image_width * self.canvas_width
    y_resized = point[1] / self.image_height * self.canvas_height
    x_original = x_resized / self.image_width * self.image.shape[1]
    y_original = y_resized / self.image_height * self.image.shape[0]

    image_row = int(x_original - (self.canvas_width-self.image_width))
    image_col = int(y_original - (self.canvas_height-self.image_height))

    return (image_row, image_col) 


# ---- Show Detected Images ----
  def open_save_window(self):
    # Open a new window for saving the image
    save_window = ctk.CTkToplevel(self.master)
    save_window.overrideredirect(True)
    save_window.geometry('500x500')
    save_window.title("Detected Image")

    self.label = ctk.CTkLabel(save_window, text='', image=self.detected_image)
    self.label.pack(fill='both', expand=True)
    save_image = ctk.CTkImage(Image.open('images/icons/download/dark.png'), size=(20, 20))
    ctk.CTkButton(
      save_window, 
      text='Save',
      border_width=1, 
      border_color=MAIN_COLOR, 
      fg_color='transparent', 
      hover_color=MAIN_COLOR, 
      border_spacing=5, 
      corner_radius=0,
      image=save_image,
      compound='right',
      command=self.save_detected_image).pack(expand=True, padx=5, pady=5)
    ctk.CTkButton(self.top, text="OK", border_width=1, border_color=MAIN_COLOR, fg_color='transparent', hover_color=MAIN_COLOR, border_spacing=5, corner_radius=0, command=self.top.destroy).pack(side='bottom', pady=10)

  def save_detected_image(self):
    file_path = filedialog.asksaveasfilename(title="Save Detected Image Image", initialfile="detection", defaultextension=self.image_extension, filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path: 
      self.pill_detected_image.save(file_path)
      success_box = CustomSuccessMessageBox(master=self, text="Detected Image Saved Successfully!", type="success")

  # ---- Replace Changes ----
  def replace_changes(self, value):
    if value in self.image_changes:
      self.image_changes.remove(value)
    self.image_changes.append(value)

  # ---- Undo Function ----
  def undo_func(self):
    if self.EDIT_FLAG.get() and len(self.image_changes) > 0:
      for key, value in self.data_vars.items():
        if self.image_changes[-1] == key:
          value[0].set(value[1])
      
      self.image_changes.pop()

      if len(self.image_changes) == 0:
        self.EDIT_FLAG.set(False)

      self.editing_image()

  # ---- Save Function ----
  def save_func(self):
    self.original = self.image
    self.image_width = self.image.shape[1]
    self.image_height = self.image.shape[0]
    self.reset_changes()
    self.display_image()

  # ---- Show Hide Undo Function ----
  def show_hide_undo(self, *args):
    self.main_window.show_hide_undo()

    self.display_image()


if __name__ == "__main__":
  Main()
