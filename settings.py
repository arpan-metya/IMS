"""				Window Configuration				"""

WINDOW_TITLE = ''

WINDOW_DISPLAY_RATIO = {'ratio': 0.75, 'minsize': (600,400)}

WINDOW_COLOR = {'background': ('#FFFFFF', '#000000'), 'main': 'transparent'}

WINDOW_ICON_PATH = {'light': 'icons/window_icon_light.ico', 'dark': 'icons/window_icon_dark.ico'}




# -------------------------------------------------------------------------------------------------------------
"""				Menu Frame Configuration				"""
# -------------------------------------------------------------------------------------------------------------




MENU_FRAME_COLOR = {'main': ('#36a4ff','#d437cc')}

# -----------------------------------------------------------------

MENU_ICON_CONFIG = {'title': '', 'corner': 10, 'width': 0, 'height': 0}

MENU_ICON_COLOR = {'background': 'transparent', 'foreground': ('black', 'white')}

MENU_ICON_PATH = {'icon': 'icons/app_icon.png'}

MENU_ICON_POSITION = {'side': 'left', 'expand': False, 'fill': None, 'anchor': 'center', 'padx': 20, 'pady': 5}

# -------------------------------------------------------------------

MENU_BUTTON_CONFIG = {'corner': 200, 'width': 50, 'height': 20, 'hover': True, 'font': ('Comic San MS', 13, 'bold')}

MENU_BUTTON_COLOR = {'background': 'transparent', 'foreground': ('#000000', '#FFFFFF'), 'hover': ('#6ebbfa', '#a827a2')}

MENU_BUTTON_PRESSED_COLOR = {'background': ('#FFFFFF','#000000'), 'foreground': ('#36a4ff', '#d437cc'), 'hover': ('#d1d1d1', '#2e2e2e')}

# MENU_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

MENU_BUTTON_POSITION = {'side': 'left', 'expand': False, 'fill': None, 'anchor': 'center', 'padx': 5, 'pady': (4,2)}

# --------------------------------------------------------------------

MODE_BUTTON_CONFIG = {'title': '', 'corner': 10, 'width': 0, 'height': 0, 'hover': False}

MODE_BUTTON_COLOR = {'background': 'transparent', 'foreground': ('black', 'white')}

MODE_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

MODE_BUTTON_POSITION = {'side': 'right', 'expand': False, 'fill': None, 'anchor': 'center', 'padx': 20, 'pady': 5}




# -------------------------------------------------------------------------------------------------------------
"""				Control Frame Configuration				"""
# -------------------------------------------------------------------------------------------------------------




CONTROL_FRAME_COLOR = {'main': 'transparent', 'profile': ('#36a4ff','#d437cc'), 'option' : ('#36a4ff','#d437cc')}

CONTROL_FRAME_POSITION = {'initial': -0.2, 'final': 0.0}

# ---------------------------------------------------------------------

CONTROL_BUTTON_CONFIG = {'corner': 200, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 15, 'bold')}

CONTROL_BUTTON_COLOR = {'background': 'transparent', 'foreground': ('#000000', '#FFFFFF'), 'hover': ('#6ebbfa', '#a827a2')}

CONTROL_BUTTON_PRESSED_COLOR = {'background': ('#FFFFFF','#000000'), 'foreground': ('#36a4ff', '#d437cc'), 'hover': ('#ececec', '#111111')}

# CONTROL_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

CONTROL_BUTTON_POSITION = {'side': 'top', 'expand': False, 'fill': 'x', 'anchor': 'e', 'padx': (10,10), 'pady': 10}




# -------------------------------------------------------------------------------------------------------------
"""				Display Frame Configuration				"""
# -------------------------------------------------------------------------------------------------------------




DISPLAY_FRAME_COLOR = {'main': 'transparent', 'page': ('#FFFFFF', '#000000')}

DISPLAY_FRAME_POSITION = {'initial': 0.0, 'final': 0.2}

# -------------------------------------------------------------------------------------------------------------

# Profile Page

# --------------------------------------------------------------------------------------------

PROFILE_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

PROFILE_LOGIN_FRAME_POSITION = (0.5, 0.5, 0.7, 0.6, 'center')

PROFILE_DETAILS_FRAME_POSITION = (0.5, 0.5, 0.95, 0.94, 'center')

# --------------------------------------------------------------------

PROFILE_BUTTON_CONFIG = {'corner': 200, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

PROFILE_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# PROFILE_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

PROFILE_LABEL_CONFIG = {'corner': 200, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

PROFILE_LABEL_VALUE_CONFIG = {'corner': 200, 'width': 0, 'height': 0, 'font': ('Comic San MS', 12)}

PROFILE_LABEL_COLOR = {'background': 'transparent', 'foreground': ('#000000', '#ffffff')}

PROFILE_LABEL_VALUE_COLOR = {'background': 'transparent', 'foreground': ('#111111', '#ececec')}

# ---------------------------------------------------------------------

PROFILE_ENTRY_CONFIG = {'corner': 200, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

PROFILE_ENTRY_COLOR = {'background': ('#ffffff', '#000000'), 'foreground': ('#111111','#2e2e2e')}

# -------------------------------------------------------------------------------------------------------------

# Employee Page

# --------------------------------------------------------------------------------------------

EMPLOYEE_LIST = [
	('User Id', 'eid', 40, 'center'), 
	('Username', 'username', 120, 'center'), 
	('First Name', 'first_name', 70, 'center'), 
	('Last Name', 'last_name', 70, 'center'), 
	('Access', 'access', 40, 'center'), 
	('Email Id', 'email_id', 150, 'center'), 
	('Phone No.', 'phone_no', 80, 'center')]

EMPLOYEE_ACCESS_LIST = ('read', 'write', 'admin')

# --------------------------------------------------------------------

EMPLOYEE_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

EMPLOYEE_CONTROL_FRAME_POSITION = (0.005, 0, 0.995, 0.195, 'nw')

EMPLOYEE_DETAILS_FRAME_POSITION = (0.005, 1, 0.995, 0.80, 'sw')

# --------------------------------------------------------------------

EMPLOYEE_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

EMPLOYEE_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# EMPLOYEE_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

EMPLOYEE_LABEL_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

EMPLOYEE_LABEL_COLOR = {'background': 'transparent', 'foreground': ('#000000','#FFFFFF')}

# ---------------------------------------------------------------------

EMPLOYEE_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

EMPLOYEE_ENTRY_COLOR = {'background': ('#ffffff', '#000000'), 'foreground': ('#111111','#2e2e2e')}

# ----------------------------------------------------------------------

EMPLOYEE_OPTIONMENU_CONFIG = {'corner': 40, 'font': ('Comic San MS', 13, 'bold')}

EMPLOYEE_OPTIONMENU_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# ---------------------------------------------------------------------------------------------

# User Page

# ---------------------------------------------------------------------------------------------


USER_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

USER_FRAME_POSITION = (0.5, 0.5, 0.9, 0.9, 'center')

# --------------------------------------------------------------------

USER_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

USER_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# USER_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

USER_LABEL_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

USER_LABEL_COLOR = {'background': 'transparent', 'foreground': ('#000000', '#ffffff')}

# ---------------------------------------------------------------------

USER_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

USER_ENTRY_COLOR = {'background': ('#ffffff', '#000000'), 'foreground': ('#111111','#2e2e2e')}

# ----------------------------------------------------------------------

USER_OPTIONMENU_CONFIG = {'corner': 80, 'font': ('Comic San MS', 13)}

USER_OPTIONMENU_COLOR = {'background': ('#d1d1d1', '#2e2e2e'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#ececec','#111111')}

# -------------------------------------------------------------------------------------------------------------

# Settings Page

# --------------------------------------------------------------------------------------------

SETTINGS_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

SETTINGS_FRAME_POSITION = (0.5, 0.5, 0.9, 0.9, 'center')

# --------------------------------------------------------------------

SETTINGS_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12)}

SETTINGS_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': None, 'hover': ('#87c9ff','#a827a2')}

# SETTINGS_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

SETTINGS_SWITCH_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12)}

SETTINGS_SWITCH_BUTTON_COLOR = {'background': ('#d1d1d1', '#2e2e2e'), 'foreground': None, 'hover': '#184034'}

SETTINGS_SWITCH_BUTTON_PROGRESS_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': None, 'hover': '#184034'}

# SETTINGS_SWITCH_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

SETTINGS_LABEL_CONFIG = {'corner': 40, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

SETTINGS_LABEL_COLOR = {'background': [('#ececec','#111111'),'transparent'], 'foreground': [('#000000','#FFFFFF'),('#2e2e2e','#ececec')]}

# ---------------------------------------------------------------------

SETTINGS_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

SETTINGS_ENTRY_COLOR = {'background': ('#FFFFFF', '#000000'), 'foreground': ('#000000','#FFFFFF')}

# ----------------------------------------------------------------------

SETTINGS_OPTIONMENU_CONFIG = {'corner': 80, 'font': ('Comic San MS', 13)}

SETTINGS_OPTIONMENU_COLOR = {'background': ('#FFFFFF', '#000000'), 'foreground': ('#000000','#FFFFFF'), 'hover': None}

# -------------------------------------------------------------------------------------------------------------

# Product Page

# --------------------------------------------------------------------------------------------

PRODUCT_LIST = [
	('Product Id', 'pid', 40, 'center'), 
	('Category', 'category', 40, 'center'),
	('Product', 'product_name', 80, 'center'), 
	('Description', 'description', 150, 'center'), 
	('Stock Qty', 'quantity', 40, 'center'), 
	('Unit Price', 'unit_price', 40, 'center'), 
	('Total Price', 'total_price', 40, 'center')] 

PRODUCT_CATEGORY_LIST = ['miscelleneous']

# --------------------------------------------------------------------

PRODUCT_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

# PRODUCT_CONTROL_FRAME_POSITION = (0.005, 0, 0.995, 0.195, 'nw')

# PRODUCT_DETAILS_FRAME_POSITION = (0.005, 1, 0.995, 0.80, 'sw')

# PRODUCT_EXTERNAL_FRAME_POSITION = (0.005, 1, 0.995, 0.80, 'sw')

# --------------------------------------------------------------------

PRODUCT_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

PRODUCT_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# PRODUCT_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

PRODUCT_LABEL_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

PRODUCT_LABEL_COLOR = {'background': 'transparent', 'foreground': ('#000000','#FFFFFF')}

# ---------------------------------------------------------------------

PRODUCT_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

PRODUCT_ENTRY_COLOR = {'background': ('#FFFFFF', '#000000'), 'foreground': ('#000000','#FFFFFF')}

# ----------------------------------------------------------------------

PRODUCT_OPTIONMENU_CONFIG = {'corner': 40, 'font': ('Comic San MS', 13, 'bold')}

PRODUCT_OPTIONMENU_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# ---------------------------------------------------------------------------------------------

# Update Page

# ---------------------------------------------------------------------------------------------


UPDATE_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

UPDATE_FRAME_POSITION = (0.5, 0.5, 0.9, 0.9, 'center')

# --------------------------------------------------------------------

UPDATE_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

UPDATE_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# UPDATE_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

UPDATE_LABEL_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13, 'bold')}

UPDATE_LABEL_COLOR = {'background': 'transparent', 'foreground': ('#000000', '#ffffff')}

# ---------------------------------------------------------------------

UPDATE_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

UPDATE_ENTRY_COLOR = {'background': ('#ffffff', '#000000'), 'foreground': ('#111111','#2e2e2e')}

# ----------------------------------------------------------------------

UPDATE_OPTIONMENU_CONFIG = {'corner': 80, 'font': ('Comic San MS', 13)}

UPDATE_OPTIONMENU_COLOR = {'background': ('#ffffff', '#000000'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# -------------------------------------------------------------------------------------------------------------

# Dashboard Page

# -------------------------------------------------------------------------------------------------------------

DASHBOARD_CATEGORY_LIST = list(PRODUCT_CATEGORY_LIST)
DASHBOARD_CATEGORY_LIST.insert(0, 'All')

# --------------------------------------------------------------------

DASHBOARD_DETAILS_FRAME_CONFIG = {'background': ('#ffffff','#000000'), 'border_width': 0, 'border_color': 'black'}

DASHBOARD_CONTROL_FRAME_CONFIG = {'background': ('#ececec','#111111'), 'border_width': 0, 'border_color': 'black'}

DASHBOARD_DETAILS_FRAME_POSITION = (0.005, 0, 0.995, 0.80, 'nw')

DASHBOARD_CONTROL_FRAME_POSITION = (0.005, 1, 0.995, 0.195, 'sw')

# --------------------------------------------------------------------

DASHBOARD_BUTTON_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'hover': True, 'font': ('Comic San MS', 12, 'bold')}

DASHBOARD_BUTTON_COLOR = {'background': ('#36a4ff', '#d437cc'), 'foreground': ('#000000', '#ffffff'), 'hover': ('#6ebbfa','#a827a2')}

# DASHBOARD_BUTTON_ICON_PATH = {'light': 'icons/dark_mode.png', 'dark': 'icons/light_mode.png'}

# ---------------------------------------------------------------------

DASHBOARD_LABEL_CONFIG = {'corner': 10, 'width': 0, 'height': 0, 'font': [('Comic San MS', 13, 'bold'),('Comic San MS', 40, 'bold')]}

DASHBOARD_LABEL_COLOR = {'background': ('#ececec','#111111'), 'foreground': ('#000000','#FFFFFF')}

# ---------------------------------------------------------------------

DASHBOARD_ENTRY_CONFIG = {'corner': 80, 'width': 0, 'height': 0, 'font': ('Comic San MS', 13)}

DASHBOARD_ENTRY_COLOR = {'background': ('#FFFFFF', '#000000'), 'foreground': ('#000000','#FFFFFF')}

# ----------------------------------------------------------------------

DASHBOARD_OPTIONMENU_CONFIG = {'corner': 20, 'font': ('Comic San MS', 13, 'bold')}

DASHBOARD_OPTIONMENU_COLOR = {'background': ('#FFFFFF', '#000000'), 'foreground': ('#000000','#FFFFFF'), 'hover': None}