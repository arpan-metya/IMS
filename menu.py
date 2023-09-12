import customtkinter as ctk
from tkinter import ttk
from settings import *
from defaults import *
from PIL import Image

class Menu(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent, fg_color = MENU_FRAME_COLOR['main'])

		# Menu frame configuration
		self.pack(expand = False, fill = 'x', padx = 4, pady = (4,2))

		# ------------------------------------------------------------------------------
		
		# attribute declaration
		try:
			self.mode_button_image = ctk.CTkImage(
				light_image = Image.open(MODE_BUTTON_ICON_PATH['light']),
				dark_image = Image.open(MODE_BUTTON_ICON_PATH['dark']))
			self.app_icon_image = ctk.CTkImage(Image.open(MENU_ICON_PATH['icon']))
		except Exception as e:
			print(e)
			self.mode_button_image = None
			MODE_BUTTON_CONFIG['title'] = 'mode'


		# widgets configuration
		self.app_icon = ctk.CTkLabel(self,
			text = MENU_ICON_CONFIG['title'],
			image = self.app_icon_image,
			corner_radius = MENU_ICON_CONFIG['corner'],
			width = MENU_ICON_CONFIG['width'],
			height = MENU_ICON_CONFIG['height'],
			fg_color = MENU_ICON_COLOR['background'],
			text_color = MENU_ICON_COLOR['foreground'])
		self.profile_button = ctk.CTkButton(self,
			text = 'Profile',
			corner_radius = MENU_BUTTON_CONFIG['corner'],
			hover = MENU_BUTTON_CONFIG['hover'],
			width = MENU_BUTTON_CONFIG['width'],
			height = MENU_BUTTON_CONFIG['height'],
			font = MENU_BUTTON_CONFIG['font'],
			fg_color = MENU_BUTTON_COLOR['background'],
			text_color = MENU_BUTTON_COLOR['foreground'],
			hover_color = MENU_BUTTON_COLOR['hover'])
		self.product_button = ctk.CTkButton(self,
			text = 'Product',
			corner_radius = MENU_BUTTON_CONFIG['corner'],
			hover = MENU_BUTTON_CONFIG['hover'],
			width = MENU_BUTTON_CONFIG['width'],
			height = MENU_BUTTON_CONFIG['height'],
			font = MENU_BUTTON_CONFIG['font'],
			fg_color = MENU_BUTTON_COLOR['background'],
			text_color = MENU_BUTTON_COLOR['foreground'],
			hover_color = MENU_BUTTON_COLOR['hover'])
		self.mode_button = ctk.CTkButton(self,
			text = MODE_BUTTON_CONFIG['title'],
			image = self.mode_button_image,
			corner_radius = MODE_BUTTON_CONFIG['corner'],
			hover = MODE_BUTTON_CONFIG['hover'],
			width = MODE_BUTTON_CONFIG['width'],
			height = MODE_BUTTON_CONFIG['height'],
			fg_color = MODE_BUTTON_COLOR['background'],
			text_color = MODE_BUTTON_COLOR['foreground'])
		# -----------------------------------------------
		self.app_icon.pack(
			side = MENU_ICON_POSITION['side'],
			expand = MENU_ICON_POSITION['expand'], 
			fill = MENU_ICON_POSITION['fill'], 
			padx = MENU_ICON_POSITION['padx'],
			pady = MENU_ICON_POSITION['pady'])
		self.profile_button.pack(
			side = MENU_BUTTON_POSITION['side'],
			expand = MENU_BUTTON_POSITION['expand'], 
			fill = MENU_BUTTON_POSITION['fill'], 
			padx = MENU_BUTTON_POSITION['padx'],
			pady = MENU_BUTTON_POSITION['pady'])
		self.product_button.pack(
			side = MENU_BUTTON_POSITION['side'],
			expand = MENU_BUTTON_POSITION['expand'], 
			fill = MENU_BUTTON_POSITION['fill'], 
			padx = MENU_BUTTON_POSITION['padx'],
			pady = MENU_BUTTON_POSITION['pady'])
		self.mode_button.pack(
			side = MODE_BUTTON_POSITION['side'],
			expand = MODE_BUTTON_POSITION['expand'], 
			fill = MODE_BUTTON_POSITION['fill'], 
			padx = MODE_BUTTON_POSITION['padx'],
			pady = MODE_BUTTON_POSITION['pady'])

		# --------------------------------------------------------------------------------

		# indicator attribute declaration
		self.pressed_button = self.profile_button
		self.pressed_indicator = 0

		# first run
		self.indicator(self.profile_button, 1)

	def indicator(self, arg, mode):
		if self.pressed_button != arg:
			self.pressed_button.configure(
				fg_color = MENU_BUTTON_COLOR['background'],
				text_color = MENU_BUTTON_COLOR['foreground'],
				hover_color = MENU_BUTTON_COLOR['hover'])
			self.pressed_button = arg
			self.pressed_button.configure(
				fg_color = MENU_BUTTON_PRESSED_COLOR['background'], 
				text_color = MENU_BUTTON_PRESSED_COLOR['foreground'], 
				hover_color = MENU_BUTTON_PRESSED_COLOR['hover'])
			self.pressed_indicator = 0
		else:
			if self.pressed_indicator == 0 and mode == 1:
				self.pressed_button.configure(
					fg_color = MENU_BUTTON_COLOR['background'], 
					text_color = MENU_BUTTON_COLOR['foreground'], 
					hover_color = MENU_BUTTON_COLOR['hover'])
				self.pressed_indicator = 1
			else:
				self.pressed_button.configure(
				fg_color = MENU_BUTTON_PRESSED_COLOR['background'], 
				text_color = MENU_BUTTON_PRESSED_COLOR['foreground'], 
				hover_color = MENU_BUTTON_PRESSED_COLOR['hover'])
				self.pressed_indicator = 0