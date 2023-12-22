# EDITING ASSETS
ROTATE_DEFAULT = 0
SCALE_FACTOR_X = 1.0
SCALE_FACTOR_Y = 1.0
FLIP_OPTIONS = ['None', 'X', 'Y', 'Both']
CROP_OPTIONS = ['None', 'Rect', 'Circle']
BRIGHTNESS_DEFAULT = 1
CONTRAST_DEFAULT = 1
BLUR_DEFAULT = 0
SHARPING_DEFAULT = 0
GRAY_LEVEL_SLICING_MIN_DEFUALT = 0
GRAY_LEVEL_SLICING_MAX_DEFUALT = 255
BIT_PLANE_SLICING_DEFUALT = 0
CONVERT_OPTIONS = ['None', 'BGR to RGB', 'BGR to Grayscale', 'RGB to BGR', 'BGR to HSV', 'BGR to LAB', 'HSV to BGR', 'Red', 'Green', 'Blue']
FILTERS_OPTIONS = ['None', 'Invert', 'Filter2D', 'Histogram Equalization', 'Logarithmic Transformation', 'Power Transformation']
DETECTION_FILTERS_OPTIONS = ['None', 'Emboss', 'Find Edges (Canny)', 'Contour', 'Threshold']
SALT_PAPPER_DEFAULT = False
MEDIAN_BLUR_DEFAULT = False
MEDIAN_KERNEL_DEFAULT = 1
VIBRANCE_DEFAULT = 1
GRAYSCALE_DEFAULT = False
INVERT_DEFAULT = False
DRAW_OPTIONS = ['None', 'Brush', 'Fill']


# PATHES
ICONS_PATH = 'images/icons'
PRELOADER_PATH = 'images/preloader.mp4'


# NAVBAR
SIDEBAR_BUTTONS = [
 {
  'name':'Position', 
  'images':{
   'light-dark': (f'{ICONS_PATH}/crop/light.png', f'{ICONS_PATH}/crop/dark.png'),
   'colored': f'{ICONS_PATH}/crop/colored.png',
   }
  },
 {
  'name':'Colors', 
  'images':{
   'light-dark': (f'{ICONS_PATH}/colors/light.png', f'{ICONS_PATH}/colors/dark.png'),
   'colored': f'{ICONS_PATH}/colors/colored.png',
   }
  },
 {
  'name':'Effects', 
  'images':{
   'light-dark': (f'{ICONS_PATH}/effects/light.png', f'{ICONS_PATH}/effects/dark.png'),
   'colored': f'{ICONS_PATH}/effects/colored.png',
   }
  },
 {
  'name':'Drawing',  
  'images':{
   'light-dark': (f'{ICONS_PATH}/brush/light.png', f'{ICONS_PATH}/brush/dark.png'),
   'colored': f'{ICONS_PATH}/brush/colored.png',
   }
  },
 {
  'name':'Detection', 
  'images':{
   'light-dark': (f'{ICONS_PATH}/ai/light.png', f'{ICONS_PATH}/ai/dark.png'),
   'colored': f'{ICONS_PATH}/ai/colored.png',
   }
  },
]

THEME_TOGGOLER_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/sun/light.png', f'{ICONS_PATH}/moon/dark.png'),
  'colored': (f'{ICONS_PATH}/sun/colored.png', f'{ICONS_PATH}/moon/colored.png')}

IMPORT_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/add/light.png', f'{ICONS_PATH}/add/dark.png'),
  'colored': f'{ICONS_PATH}/add/colored.png'}

CLOSE_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/close/light.png', f'{ICONS_PATH}/close/dark.png'),
  'colored': f'{ICONS_PATH}/close/colored.png'}

EXPAND_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/expand/light.png', f'{ICONS_PATH}/expand/dark.png'),
  'colored': f'{ICONS_PATH}/expand/colored.png'}

UNDO_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/rotate/light.png', f'{ICONS_PATH}/rotate/dark.png'),
  'colored': f'{ICONS_PATH}/rotate/colored.png'}

EXPORT_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/download/light.png', f'{ICONS_PATH}/download/dark.png'),
  'colored': f'{ICONS_PATH}/download/colored.png'}

SAVE_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/correct/light.png', f'{ICONS_PATH}/correct/dark.png'),
  'colored': f'{ICONS_PATH}/correct/colored.png'}

SUCCESS_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/success/light.png', f'{ICONS_PATH}/success/dark.png'),
  'colored': f'{ICONS_PATH}/success/colored.png'}

WARNING_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/warning/light.png', f'{ICONS_PATH}/warning/dark.png'),
  'colored': f'{ICONS_PATH}/warning/colored.png'}

INFO_IMAGE = {
  'light-dark': (f'{ICONS_PATH}/info/light.png', f'{ICONS_PATH}/info/dark.png'),
  'colored': f'{ICONS_PATH}/info/colored.png'}

COLOR_PICKER_IMAGE = f'{ICONS_PATH}/colors/wheel.png'

# COLORS
MAIN_COLOR = '#45f3ff'
SECOND_COLOR = '#00e8f8'
RED_COLOR = '#8A0606'
LIGHT = ('#EEEEEE', '#022c43')
DARK = ('#022c43', '#EEEEEE')
BACKGOUND_COLOR = ('#f1f1f1', '#242424')
SIDEBAR_COLOR = ('#dddddd', '#333333')
CONTROL_COLOR = ('#eeeeee', '#4A4A4A')


# FONTS 
FONT_FAMILY = 'Helvetica'
SMALL_FONT_SIZE = 18
MEDIUM_FONT_SIZE = 20
LARGE_FONT_SIZE = 22
