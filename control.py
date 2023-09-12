import customtkinter as ctk
from tkinter import ttk
from settings import *
from defaults import *

class Control(ctk.CTkFrame):
	def __init__(self, parent, initial = CONTROL_FRAME_POSITION['initial'], final = CONTROL_FRAME_POSITION['final']):
		super().__init__(parent, fg_color = CONTROL_FRAME_COLOR['main'])

		# attribute declaration
		self.initial = initial
		self.final = final
		self.width = abs(final-initial)

		# Control frame configuration
		self.place(relx = self.initial, rely = 0, relwidth = self.width, relheight = 1)

		# ----------------------------------------------------------------------------------

		# child frame declaration
		self.profile = Profile(self)
		self.option = Option(self)

		# ----------------------------------------------------------------------------------

		# indicator attribute declaration
		self.pressed_button = self.profile.profile_button

		# first run
		self.indicator(self.profile.profile_button)

		# ----------------------------------------------------------------------------------

	def indicator(self, arg):
		if self.pressed_button != arg:
			self.pressed_button.configure(
				fg_color = CONTROL_BUTTON_COLOR['background'],
				text_color = CONTROL_BUTTON_COLOR['foreground'],
				hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.pressed_button = arg
		arg.configure(
			fg_color = CONTROL_BUTTON_PRESSED_COLOR['background'], 
			text_color = CONTROL_BUTTON_PRESSED_COLOR['foreground'], 
			hover_color = CONTROL_BUTTON_PRESSED_COLOR['hover'])



class Profile(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = CONTROL_FRAME_COLOR['profile'])
		
		# widgets configuration
		self.user_button = ctk.CTkButton(self,
			text = 'Create/Update User',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.profile_button = ctk.CTkButton(self,
			text = 'Profile Login',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.employee_button = ctk.CTkButton(self,
			text = 'Manage User',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.settings_button = ctk.CTkButton(self,
			text = 'Settings',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		# -------------------------------------------------
		self.profile_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = (20,CONTROL_BUTTON_POSITION['pady']),
			anchor = CONTROL_BUTTON_POSITION['anchor'])
		self.user_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = CONTROL_BUTTON_POSITION['pady'],
			anchor = CONTROL_BUTTON_POSITION['anchor'])
		self.employee_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = CONTROL_BUTTON_POSITION['pady'],
			anchor = CONTROL_BUTTON_POSITION['anchor'])
		self.settings_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = CONTROL_BUTTON_POSITION['pady'],
			anchor = CONTROL_BUTTON_POSITION['anchor'])



class Option(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = CONTROL_FRAME_COLOR['option'])

		# attribute declaration


		# widgets configuration
		self.dashboard_button = ctk.CTkButton(self,
			text = 'Dashboard',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.product_button = ctk.CTkButton(self,
			text = 'Manage Product',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		self.update_button = ctk.CTkButton(self,
			text = 'Add/Update Product',
			corner_radius = CONTROL_BUTTON_CONFIG['corner'],
			hover = CONTROL_BUTTON_CONFIG['hover'],
			font = CONTROL_BUTTON_CONFIG['font'],
			fg_color = CONTROL_BUTTON_COLOR['background'],
			text_color = CONTROL_BUTTON_COLOR['foreground'],
			hover_color = CONTROL_BUTTON_COLOR['hover'])
		# -------------------------------------------------
		self.dashboard_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = (20,CONTROL_BUTTON_POSITION['pady']),
			anchor = CONTROL_BUTTON_POSITION['anchor'])
		self.product_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = CONTROL_BUTTON_POSITION['pady'],
			anchor = CONTROL_BUTTON_POSITION['anchor'])
		self.update_button.pack(
			side = CONTROL_BUTTON_POSITION['side'],
			expand = CONTROL_BUTTON_POSITION['expand'], 
			fill = CONTROL_BUTTON_POSITION['fill'], 
			padx = CONTROL_BUTTON_POSITION['padx'],
			pady = CONTROL_BUTTON_POSITION['pady'],
			anchor = CONTROL_BUTTON_POSITION['anchor'])

