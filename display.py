import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from settings import *
from defaults import *

class Display(ctk.CTkFrame):
	def __init__(self, parent, initial = DISPLAY_FRAME_POSITION['initial'], final = DISPLAY_FRAME_POSITION['final']):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['main'])

		# attribute declaration
		self.initial = initial
		self.final = final
		# self.width = abs(1.0-initial)

		# Display frame configuration
		self.place(relx = self.initial, 
			rely = 0, 
			relwidth = abs(1.0-self.initial), 
			relheight = 1)

		# -------------------------------------------------------------------------------------------

		# child frame declaration
		self.user_page = User_Page(self)
		self.profile_page = Profile_Page(self)
		self.employee_page = Employee_Page(self)
		self.settings_page = Settings_Page(self)
		self.dashboard_page = Dashboard_Page(self)
		self.product_page = Product_Page(self)
		self.update_page = Update_Page(self)

		# -------------------------------------------------------------------------------------------

		# total price calculation per product
		self.update_page.update_total_price_button.configure(command = lambda: self.calculate_total_price())

	def calculate_total_price(self):
		try:
			total_price = float(self.update_page.quantity.get()) * float(self.update_page.unit_price.get())
			self.update_page.total_price.set(str(round(total_price, 2)))
		except Exception as e:
			messagebox.showerror('Error', 'Wrong Data Type in Quantity/Unit Price')


class User_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.user_frame = ctk.CTkFrame(self,
			fg_color = USER_FRAME_CONFIG['background'],
			border_width = USER_FRAME_CONFIG['border_width'],
			border_color = USER_FRAME_CONFIG['border_color'])
		self.user_frame.place(
			relx = USER_FRAME_POSITION[0], 
			rely = USER_FRAME_POSITION[1], 
			relwidth = USER_FRAME_POSITION[2], 
			relheight = USER_FRAME_POSITION[3], 
			anchor = USER_FRAME_POSITION[4])

		# child frame configuration
		self.user_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
		self.user_frame.columnconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')

		# ----------------------------------------------------------------------------------------

		# attribute declaration
		access_list = EMPLOYEE_ACCESS_LIST
		self.user = ctk.StringVar(value = '')
		self.access = ctk.StringVar(value = '')
		self.username = ctk.StringVar(value = '')
		self.password = ctk.StringVar(value = '')
		self.first = ctk.StringVar(value = '')
		self.last = ctk.StringVar(value = '')
		self.email = ctk.StringVar(value = '')
		self.phone = ctk.StringVar(value = '')

		# ----------------------------------------------------------------------------------------

		# widgets configuration
		self.user_id_label = ctk.CTkLabel(self.user_frame,
			text = 'User Id :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_id_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.user,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_access_label = ctk.CTkLabel(self.user_frame,
			text = 'Access :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_access_optionmenu = ctk.CTkOptionMenu(self.user_frame,
			values = access_list,
			corner_radius = USER_OPTIONMENU_CONFIG['corner'],
			font = USER_OPTIONMENU_CONFIG['font'],
			dropdown_font = USER_OPTIONMENU_CONFIG['font'],
			state = 'readonly',
			variable = self.access,
			fg_color = USER_OPTIONMENU_COLOR['background'],
			dropdown_fg_color = USER_OPTIONMENU_COLOR['background'],
			button_color = USER_OPTIONMENU_COLOR['background'],
			text_color = USER_OPTIONMENU_COLOR['foreground'],
			dropdown_text_color = USER_OPTIONMENU_COLOR['foreground'])
		self.user_first_label = ctk.CTkLabel(self.user_frame,
			text = 'First Name :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_first_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.first,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_last_label = ctk.CTkLabel(self.user_frame,
			text = 'Last Name :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_last_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.last,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_email_label = ctk.CTkLabel(self.user_frame,
			text = 'Email Id :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_email_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.email,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_phone_label = ctk.CTkLabel(self.user_frame,
			text = 'Phone No. :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_phone_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.phone,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_username_label = ctk.CTkLabel(self.user_frame,
			text = 'username :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_username_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.username,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_password_label = ctk.CTkLabel(self.user_frame,
			text = 'password :',
			corner_radius = USER_LABEL_CONFIG['corner'],
			font = USER_LABEL_CONFIG['font'],
			fg_color = USER_LABEL_COLOR['background'],
			text_color = USER_LABEL_COLOR['foreground'])
		self.user_password_entry = ctk.CTkEntry(self.user_frame,
			textvariable = self.password,
			corner_radius = USER_ENTRY_CONFIG['corner'],
			font = USER_ENTRY_CONFIG['font'],
			fg_color = USER_ENTRY_COLOR['background'])
		self.user_create_button = ctk.CTkButton(self.user_frame, 
			text = 'Create User',
			corner_radius = USER_BUTTON_CONFIG['corner'],
			hover = USER_BUTTON_CONFIG['hover'],
			font = USER_BUTTON_CONFIG['font'],
			fg_color = USER_BUTTON_COLOR['background'],
			text_color = USER_BUTTON_COLOR['foreground'],
			hover_color = USER_BUTTON_COLOR['hover'])
		self.user_update_button = ctk.CTkButton(self.user_frame, 
			text = 'Update User',
			corner_radius = USER_BUTTON_CONFIG['corner'],
			hover = USER_BUTTON_CONFIG['hover'],
			font = USER_BUTTON_CONFIG['font'],
			state = 'disabled',
			fg_color = USER_BUTTON_COLOR['background'],
			text_color = USER_BUTTON_COLOR['foreground'],
			hover_color = USER_BUTTON_COLOR['hover'])

		# ----------------------------------------------------------------------------------------
		self.user_id_label.grid(
			row = 0,
			column = 0,
			sticky= 'e',
			padx = (10,5),
			pady = (20,10))
		self.user_id_entry.grid(
			row = 0,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (20,10))
		self.user_access_label.grid(
			row = 0,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (20,10))
		self.user_access_optionmenu.grid(
			row = 0,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (20,10))
		self.user_first_label.grid(
			row = 1,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.user_first_entry.grid(
			row = 1,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (10,10))
		self.user_last_label.grid(
			row = 1,
			column = 3,
			sticky ='e',
			padx = (5,5),
			pady = (10,10))
		self.user_last_entry.grid(
			row = 1,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))
		self.user_email_label.grid(
			row = 2,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.user_email_entry.grid(
			row = 2,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (10,10))
		self.user_phone_label.grid(
			row = 2,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (10,10))
		self.user_phone_entry.grid(
			row = 2,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))
		self.user_username_label.grid(
			row = 3,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.user_username_entry.grid(
			row = 3,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (10,10))
		self.user_password_label.grid(
			row = 3,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (10,10))
		self.user_password_entry.grid(
			row = 3,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))
		self.user_create_button.grid(
			row = 4,
			column = 1,
			columnspan = 2,
			padx = 10,
			pady = 10)
		self.user_update_button.grid(
			row = 4,
			column = 3,
			columnspan = 2,
			padx = 10,
			pady = 10)


class Profile_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.profile_login_frame = ctk.CTkFrame(self,
			fg_color = PROFILE_FRAME_CONFIG['background'],
			border_width = PROFILE_FRAME_CONFIG['border_width'],
			border_color = PROFILE_FRAME_CONFIG['border_color'])
		self.profile_login_frame.place(
			relx = PROFILE_LOGIN_FRAME_POSITION[0], 
			rely = PROFILE_LOGIN_FRAME_POSITION[1], 
			relwidth = PROFILE_LOGIN_FRAME_POSITION[2], 
			relheight = PROFILE_LOGIN_FRAME_POSITION[3], 
			anchor = PROFILE_LOGIN_FRAME_POSITION[4])

		self.profile_user_frame = ctk.CTkFrame(self,
			fg_color = PROFILE_FRAME_CONFIG['background'],
			border_width = PROFILE_FRAME_CONFIG['border_width'],
			border_color = PROFILE_FRAME_CONFIG['border_color'])

		# child frame configuration
		self.profile_login_frame.rowconfigure((0,1,2), weight = 1, uniform = 'a')
		self.profile_login_frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')

		# -------------------------------------------------------------------------------------------

		# attribute declaration
		self.username = ctk.StringVar()
		self.password = ctk.StringVar()

		self.id = ctk.StringVar(value = '--')
		self.user = ctk.StringVar(value = '--')
		self.name = ctk.StringVar(value = '--')
		self.access = ctk.StringVar(value = '--')
		self.email = ctk.StringVar(value = '--')
		self.phone = ctk.StringVar(value = '--')

		# -------------------------------------------------------------------------------------------

		# widgets configuration
		self.profile_username_label = ctk.CTkLabel(self.profile_login_frame,
			text = 'username :',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_username_entry = ctk.CTkEntry(self.profile_login_frame,
			textvariable = self.username,
			corner_radius = PROFILE_ENTRY_CONFIG['corner'],
			font = PROFILE_ENTRY_CONFIG['font'],
			fg_color = PROFILE_ENTRY_COLOR['background'])
		self.profile_password_label = ctk.CTkLabel(self.profile_login_frame,
			text = 'password :',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_password_entry = ctk.CTkEntry(self.profile_login_frame,
			textvariable = self.password,
			corner_radius = PROFILE_ENTRY_CONFIG['corner'],
			font = PROFILE_ENTRY_CONFIG['font'],
			show = '*',
			fg_color = PROFILE_ENTRY_COLOR['background'])
		self.profile_login_button = ctk.CTkButton(self.profile_login_frame, 
			text = 'Log in',
			corner_radius = PROFILE_BUTTON_CONFIG['corner'],
			hover = PROFILE_BUTTON_CONFIG['hover'],
			font = PROFILE_BUTTON_CONFIG['font'],
			fg_color = PROFILE_BUTTON_COLOR['background'],
			text_color = PROFILE_BUTTON_COLOR['foreground'],
			hover_color = PROFILE_BUTTON_COLOR['hover'])

		# --------------------------------------------------------------------------------------------
		
		self.profile_username_label.grid(
			row = 0,
			column = 0,
			columnspan = 1,
			sticky = 'e',
			padx = (0,5),
			pady = (20,10))
		self.profile_username_entry.grid(
			row = 0,
			column = 1,
			columnspan = 3,
			sticky = 'ew',
			padx = (0,60),
			pady = (20,10))
		self.profile_password_label.grid(
			row = 1,
			column = 0,
			columnspan = 1,
			sticky = 'e',
			padx = (0,5),
			pady = 10)
		self.profile_password_entry.grid(
			row = 1,
			column = 1,
			columnspan = 3,
			sticky = 'ew',
			padx = (0,60),
			pady = 10)
		self.profile_login_button.grid(
			row = 2,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (20,10),
			pady = (10,20))

		# -----------------------------------------------------------------------------------------------
		
		self.profile_id_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'User Id',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_id_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.id,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_user_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'username',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_user_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.user,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_name_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'Full Name',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_name_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.name,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_access_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'Access',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_access_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.access,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_email_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'Email',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_email_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.email,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_phone_label = ctk.CTkLabel(self.profile_user_frame,
			text = 'Phone',
			corner_radius = PROFILE_LABEL_CONFIG['corner'],
			font = PROFILE_LABEL_CONFIG['font'],
			fg_color = PROFILE_LABEL_COLOR['background'],
			text_color = PROFILE_LABEL_COLOR['foreground'])
		self.profile_phone_val_label = ctk.CTkLabel(self.profile_user_frame,
			textvariable = self.phone,
			corner_radius = PROFILE_LABEL_VALUE_CONFIG['corner'],
			font = PROFILE_LABEL_VALUE_CONFIG['font'],
			fg_color = PROFILE_LABEL_VALUE_COLOR['background'],
			text_color = PROFILE_LABEL_VALUE_COLOR['foreground'])
		self.profile_logout_button = ctk.CTkButton(self.profile_user_frame, 
			text = 'Log out',
			corner_radius = PROFILE_BUTTON_CONFIG['corner'],
			hover = PROFILE_BUTTON_CONFIG['hover'],
			font = PROFILE_BUTTON_CONFIG['font'],
			fg_color = PROFILE_BUTTON_COLOR['background'],
			text_color = PROFILE_BUTTON_COLOR['foreground'],
			hover_color = PROFILE_BUTTON_COLOR['hover'])

		# ------------------------------------------------------------------------------------------	
		
		self.profile_id_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = (5,1))
		self.profile_id_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_user_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_user_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_name_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_name_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_access_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_access_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_email_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_email_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_phone_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_phone_val_label.pack(
			expand = True,
			fill = 'x',
			padx = 20, 
			pady = 1)
		self.profile_logout_button.pack(
			side = 'bottom',
			expand = True,
			padx = 20, 
			pady = (10,10))
		# --------------------------------------------------------------------------------------------


class Employee_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.employee_control_frame = ctk.CTkFrame(self,
			fg_color = EMPLOYEE_FRAME_CONFIG['background'],
			border_width = EMPLOYEE_FRAME_CONFIG['border_width'],
			border_color = EMPLOYEE_FRAME_CONFIG['border_color'])
		self.employee_control_frame.place(
			relx = EMPLOYEE_CONTROL_FRAME_POSITION[0], 
			rely = EMPLOYEE_CONTROL_FRAME_POSITION[1], 
			relwidth = EMPLOYEE_CONTROL_FRAME_POSITION[2], 
			relheight = EMPLOYEE_CONTROL_FRAME_POSITION[3], 
			anchor = EMPLOYEE_CONTROL_FRAME_POSITION[4])

		self.employee_details_frame = ctk.CTkFrame(self,
			fg_color = EMPLOYEE_FRAME_CONFIG['background'],
			border_width = EMPLOYEE_FRAME_CONFIG['border_width'],
			border_color = EMPLOYEE_FRAME_CONFIG['border_color'])
		self.employee_details_frame.place(
			relx = EMPLOYEE_DETAILS_FRAME_POSITION[0], 
			rely = EMPLOYEE_DETAILS_FRAME_POSITION[1], 
			relwidth = EMPLOYEE_DETAILS_FRAME_POSITION[2], 
			relheight = EMPLOYEE_DETAILS_FRAME_POSITION[3], 
			anchor = EMPLOYEE_DETAILS_FRAME_POSITION[4])

		# child frame configuration
		self.employee_control_frame.rowconfigure((0,1), weight = 1, uniform = 'a')
		self.employee_control_frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')

		# -------------------------------------------------------------------------------------------

		# attribute declaration
		self.search_field = ctk.StringVar(value = EMPLOYEE_LIST[0][0])
		self.search_value = ctk.StringVar()
		e_LIST = []
		e_list = []
		for item in EMPLOYEE_LIST:
			e_LIST.append(item[0])
			e_list.append(item[1])

		# widgets configuration
		self.employee_search_optionmenu = ctk.CTkOptionMenu(self.employee_control_frame,
			values = e_LIST,
			corner_radius = EMPLOYEE_OPTIONMENU_CONFIG['corner'],
			font = EMPLOYEE_OPTIONMENU_CONFIG['font'],
			dropdown_font = EMPLOYEE_OPTIONMENU_CONFIG['font'],
			state = 'readonly',
			variable = self.search_field,
			fg_color = EMPLOYEE_OPTIONMENU_COLOR['background'],
			dropdown_fg_color = EMPLOYEE_OPTIONMENU_COLOR['background'],
			button_color = EMPLOYEE_OPTIONMENU_COLOR['background'],
			text_color = EMPLOYEE_OPTIONMENU_COLOR['foreground'],
			dropdown_text_color = EMPLOYEE_OPTIONMENU_COLOR['foreground'])
		self.employee_search_entry = ctk.CTkEntry(self.employee_control_frame,
			textvariable = self.search_value,
			corner_radius = EMPLOYEE_ENTRY_CONFIG['corner'],
			font = EMPLOYEE_ENTRY_CONFIG['font'],
			fg_color = EMPLOYEE_ENTRY_COLOR['background'])
		self.employee_search_button = ctk.CTkButton(self.employee_control_frame,
			text = 'Search',
			corner_radius = EMPLOYEE_BUTTON_CONFIG['corner'],
			hover = EMPLOYEE_BUTTON_CONFIG['hover'],
			font = EMPLOYEE_BUTTON_CONFIG['font'],
			fg_color = EMPLOYEE_BUTTON_COLOR['background'],
			text_color = EMPLOYEE_BUTTON_COLOR['foreground'],
			hover_color = EMPLOYEE_BUTTON_COLOR['hover'])
		self.employee_refresh_button = ctk.CTkButton(self.employee_control_frame,
			text = 'Refresh',
			corner_radius = EMPLOYEE_BUTTON_CONFIG['corner'],
			hover = EMPLOYEE_BUTTON_CONFIG['hover'],
			font = EMPLOYEE_BUTTON_CONFIG['font'],
			fg_color = EMPLOYEE_BUTTON_COLOR['background'],
			text_color = EMPLOYEE_BUTTON_COLOR['foreground'],
			hover_color = EMPLOYEE_BUTTON_COLOR['hover'])
		self.employee_create_button = ctk.CTkButton(self.employee_control_frame,
			text = 'Create',
			corner_radius = EMPLOYEE_BUTTON_CONFIG['corner'],
			hover = EMPLOYEE_BUTTON_CONFIG['hover'],
			font = EMPLOYEE_BUTTON_CONFIG['font'],
			fg_color = EMPLOYEE_BUTTON_COLOR['background'],
			text_color = EMPLOYEE_BUTTON_COLOR['foreground'],
			hover_color = EMPLOYEE_BUTTON_COLOR['hover'])
		self.employee_update_button = ctk.CTkButton(self.employee_control_frame,
			text = 'Update',
			corner_radius = EMPLOYEE_BUTTON_CONFIG['corner'],
			hover = EMPLOYEE_BUTTON_CONFIG['hover'],
			font = EMPLOYEE_BUTTON_CONFIG['font'],
			fg_color = EMPLOYEE_BUTTON_COLOR['background'],
			text_color = EMPLOYEE_BUTTON_COLOR['foreground'],
			hover_color = EMPLOYEE_BUTTON_COLOR['hover'])
		self.employee_delete_button = ctk.CTkButton(self.employee_control_frame,
			text = 'Delete',
			corner_radius = EMPLOYEE_BUTTON_CONFIG['corner'],
			hover = EMPLOYEE_BUTTON_CONFIG['hover'],
			font = EMPLOYEE_BUTTON_CONFIG['font'],
			fg_color = EMPLOYEE_BUTTON_COLOR['background'],
			text_color = EMPLOYEE_BUTTON_COLOR['foreground'],
			hover_color = EMPLOYEE_BUTTON_COLOR['hover'])

		# --------------------------------------------------------------------------------------------
		
		self.employee_search_optionmenu.grid(
			row = 0,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.employee_search_entry.grid(
			row = 0,
			column = 1,
			columnspan = 2,
			sticky = 'ew')
		self.employee_search_button.grid(
			row = 0,
			column = 3,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.employee_refresh_button.grid(
			row = 1,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.employee_create_button.grid(
			row = 1,
			column = 1,
			# sticky = 'ew',
			padx = (0,10),
			pady = 10)
		self.employee_update_button.grid(
			row = 1,
			column = 2,
			# sticky = 'ew',
			pady = 10)
		self.employee_delete_button.grid(
			row = 1,
			column = 3,
			# sticky = 'ew',
			padx = 10,
			pady = 10)

		# -------------------------------------------------------------------------------------------

		# table declaration
		self.employee_table = ttk.Treeview(self.employee_details_frame,
			columns = e_list,
			show = 'headings')
		self.employee_table.heading(EMPLOYEE_LIST[0][1], 
			text = EMPLOYEE_LIST[0][0])
		self.employee_table.column(EMPLOYEE_LIST[0][1], 
			width = EMPLOYEE_LIST[0][2], 
			anchor = EMPLOYEE_LIST[0][3])
		self.employee_table.heading(EMPLOYEE_LIST[1][1], 
			text = EMPLOYEE_LIST[1][0])
		self.employee_table.column(EMPLOYEE_LIST[1][1], 
			width = EMPLOYEE_LIST[1][2], 
			anchor = EMPLOYEE_LIST[1][3])
		self.employee_table.heading(EMPLOYEE_LIST[2][1], 
			text = EMPLOYEE_LIST[2][0])
		self.employee_table.column(EMPLOYEE_LIST[2][1], 
			width = EMPLOYEE_LIST[2][2], 
			anchor = EMPLOYEE_LIST[2][3])
		self.employee_table.heading(EMPLOYEE_LIST[3][1], 
			text = EMPLOYEE_LIST[3][0])
		self.employee_table.column(EMPLOYEE_LIST[3][1], 
			width = EMPLOYEE_LIST[3][2], 
			anchor = EMPLOYEE_LIST[3][3])
		self.employee_table.heading(EMPLOYEE_LIST[4][1], 
			text = EMPLOYEE_LIST[4][0])
		self.employee_table.column(EMPLOYEE_LIST[4][1], 
			width = EMPLOYEE_LIST[4][2], 
			anchor = EMPLOYEE_LIST[4][3])
		self.employee_table.heading(EMPLOYEE_LIST[5][1], 
			text = EMPLOYEE_LIST[5][0])
		self.employee_table.column(EMPLOYEE_LIST[5][1], 
			width = EMPLOYEE_LIST[5][2], 
			anchor = EMPLOYEE_LIST[5][3])
		self.employee_table.heading(EMPLOYEE_LIST[6][1], 
			text = EMPLOYEE_LIST[6][0])
		self.employee_table.column(EMPLOYEE_LIST[6][1], 
			width = EMPLOYEE_LIST[6][2], 
			anchor = EMPLOYEE_LIST[6][3])
		
		self.employee_scrollbar = ctk.CTkScrollbar(
			self.employee_details_frame,
			command = self.employee_table.yview)
		self.employee_table.configure(yscrollcommand = self.employee_scrollbar.set)

		# -------------------------------------------------------------------------------------------
		
		self.employee_table.pack(
			expand = True,
			fill = 'both',
			padx = 5,
			pady = 5)
		self.employee_scrollbar.place(
			relx = 1,
			rely = 0,
			relheight = 1,
			anchor = 'ne')


class Settings_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame and widget declaration
		self.settings_appearance_label = ctk.CTkLabel(self,
			text = 'Appearance',
			corner_radius = SETTINGS_LABEL_CONFIG['corner'],
			font = SETTINGS_LABEL_CONFIG['font'],
			fg_color = SETTINGS_LABEL_COLOR['background'][0],
			text_color = SETTINGS_LABEL_COLOR['foreground'][0])
		self.settings_frame = ctk.CTkFrame(self,
			fg_color = SETTINGS_FRAME_CONFIG['background'],
			border_width = SETTINGS_FRAME_CONFIG['border_width'],
			border_color = SETTINGS_FRAME_CONFIG['border_color'])

		self.settings_appearance_label.pack(
			fill = 'x',
			expand = False,
			anchor = 'center',
			padx = 20,
			pady = (15,2))
		self.settings_frame.pack(
			fill = 'both',
			expand = True,
			padx = 20,
			pady = 2)

		# child frame configuration
		# self.settings_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
		self.settings_frame.columnconfigure((0,1), weight = 1, uniform = 'a')

		# -------------------------------------------------------------------------------------------------------

		# animation button declaration
		self.animation = ctk.BooleanVar(value = DEFAULT_ANIMATION)
		self.fullscreen = ctk.BooleanVar(value = DEFAULT_FULLSCREEN)
		self.titlebar = ctk.BooleanVar(value = DEFAULT_HIDE_TITLEBAR)

		# widgets configuration
		self.settings_titlebar_label = ctk.CTkLabel(self.settings_frame,
			text = 'Switch Titlebar Appearance',
			corner_radius = SETTINGS_LABEL_CONFIG['corner'],
			font = SETTINGS_LABEL_CONFIG['font'],
			fg_color = SETTINGS_LABEL_COLOR['background'][1],
			text_color = SETTINGS_LABEL_COLOR['foreground'][1])
		self.settings_titlebar_button = ctk.CTkSwitch(self.settings_frame, 
			text = '', 
			variable = self.titlebar, 
			onvalue = True, 
			offvalue = False,
			corner_radius = SETTINGS_SWITCH_BUTTON_CONFIG['corner'],
			font = SETTINGS_SWITCH_BUTTON_CONFIG['font'],
			fg_color = SETTINGS_SWITCH_BUTTON_COLOR['background'],
			progress_color = SETTINGS_SWITCH_BUTTON_PROGRESS_COLOR['background'],
			button_color = SETTINGS_BUTTON_COLOR['background'],
			button_hover_color = SETTINGS_BUTTON_COLOR['hover'])
		self.settings_fullscreen_label = ctk.CTkLabel(self.settings_frame,
			text = 'Switch to Fullscreen',
			corner_radius = SETTINGS_LABEL_CONFIG['corner'],
			font = SETTINGS_LABEL_CONFIG['font'],
			fg_color = SETTINGS_LABEL_COLOR['background'][1],
			text_color = SETTINGS_LABEL_COLOR['foreground'][1])
		self.settings_fullscreen_button = ctk.CTkSwitch(self.settings_frame, 
			text = '', 
			variable = self.fullscreen, 
			onvalue = True, 
			offvalue = False,
			corner_radius = SETTINGS_SWITCH_BUTTON_CONFIG['corner'],
			font = SETTINGS_SWITCH_BUTTON_CONFIG['font'],
			fg_color = SETTINGS_SWITCH_BUTTON_COLOR['background'],
			progress_color = SETTINGS_SWITCH_BUTTON_PROGRESS_COLOR['background'],
			button_color = SETTINGS_BUTTON_COLOR['background'],
			button_hover_color = SETTINGS_BUTTON_COLOR['hover'])
		self.settings_animation_label = ctk.CTkLabel(self.settings_frame,
			text = 'Switch to Wideview',
			corner_radius = SETTINGS_LABEL_CONFIG['corner'],
			font = SETTINGS_LABEL_CONFIG['font'],
			fg_color = SETTINGS_LABEL_COLOR['background'][1],
			text_color = SETTINGS_LABEL_COLOR['foreground'][1])
		self.settings_animation_button = ctk.CTkSwitch(self.settings_frame, 
			text = '', 
			variable = self.animation, 
			onvalue = True, 
			offvalue = False,
			corner_radius = SETTINGS_SWITCH_BUTTON_CONFIG['corner'],
			font = SETTINGS_SWITCH_BUTTON_CONFIG['font'],
			fg_color = SETTINGS_SWITCH_BUTTON_COLOR['background'],
			progress_color = SETTINGS_SWITCH_BUTTON_PROGRESS_COLOR['background'],
			button_color = SETTINGS_BUTTON_COLOR['background'],
			button_hover_color = SETTINGS_BUTTON_COLOR['hover'])

		# ----------------------------------------------------------------------------------------------------------

		self.settings_titlebar_label.grid(
			row = 0,
			column = 0,
			sticky = 'w',
			padx = 50,
			pady = (10,5))
		self.settings_titlebar_button.grid(
			row = 0,
			column = 1,
			sticky = 'e',
			padx = 5,
			pady = (10,5))
		self.settings_fullscreen_label.grid(
			row = 1,
			column = 0,
			sticky = 'w',
			padx = 50,
			pady = 5)
		self.settings_fullscreen_button.grid(
			row = 1,
			column = 1,
			sticky = 'e',
			padx = 5,
			pady = 5)
		self.settings_animation_label.grid(
			row = 2,
			column = 0,
			sticky = 'w',
			padx = 50,
			pady = 5)
		self.settings_animation_button.grid(
			row = 2,
			column = 1,
			sticky = 'e',
			padx = 5,
			pady = 5)


class Dashboard_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.dashboard_control_frame = ctk.CTkFrame(self,
			fg_color = DASHBOARD_CONTROL_FRAME_CONFIG['background'],
			border_width = DASHBOARD_CONTROL_FRAME_CONFIG['border_width'],
			border_color = DASHBOARD_CONTROL_FRAME_CONFIG['border_color'])
		self.dashboard_control_frame.place(
			relx = DASHBOARD_CONTROL_FRAME_POSITION[0], 
			rely = DASHBOARD_CONTROL_FRAME_POSITION[1], 
			relwidth = DASHBOARD_CONTROL_FRAME_POSITION[2], 
			relheight = DASHBOARD_CONTROL_FRAME_POSITION[3], 
			anchor = DASHBOARD_CONTROL_FRAME_POSITION[4])

		self.dashboard_details_frame = ctk.CTkFrame(self,
			fg_color = DASHBOARD_DETAILS_FRAME_CONFIG['background'],
			border_width = DASHBOARD_DETAILS_FRAME_CONFIG['border_width'],
			border_color = DASHBOARD_DETAILS_FRAME_CONFIG['border_color'])
		self.dashboard_details_frame.place(
			relx = DASHBOARD_DETAILS_FRAME_POSITION[0], 
			rely = DASHBOARD_DETAILS_FRAME_POSITION[1], 
			relwidth = DASHBOARD_DETAILS_FRAME_POSITION[2], 
			relheight = DASHBOARD_DETAILS_FRAME_POSITION[3], 
			anchor = DASHBOARD_DETAILS_FRAME_POSITION[4])

		# child frame configuration
		self.dashboard_control_frame.rowconfigure((0,1), weight = 1, uniform = 'a')
		self.dashboard_control_frame.columnconfigure((0,1), weight = 1, uniform = 'a')

		self.dashboard_details_frame.rowconfigure((0,1), weight = 1, uniform = 'a')
		self.dashboard_details_frame.columnconfigure((0,1), weight = 1, uniform = 'a')

		# --------------------------------------------------------------------------------------------

		# attribute declaration
		category_list = DASHBOARD_CATEGORY_LIST
		self.category = ctk.StringVar(value = DASHBOARD_CATEGORY_LIST[0])
		self.quantity_val = ctk.StringVar(value = '-')
		self.price_val = ctk.StringVar(value = '-')

		# widgets configuration
		self.dashboard_category_label = ctk.CTkLabel(self.dashboard_control_frame,
			text = 'Choose Category',
			corner_radius = DASHBOARD_LABEL_CONFIG['corner'],
			font = DASHBOARD_LABEL_CONFIG['font'][0],
			fg_color = DASHBOARD_LABEL_COLOR['background'],
			text_color = DASHBOARD_LABEL_COLOR['foreground'])
		self.dashboard_category_optionmenu = ctk.CTkOptionMenu(self.dashboard_control_frame,
			values = category_list,
			corner_radius = DASHBOARD_OPTIONMENU_CONFIG['corner'],
			font = DASHBOARD_OPTIONMENU_CONFIG['font'],
			dropdown_font = DASHBOARD_OPTIONMENU_CONFIG['font'],
			state = 'readonly',
			variable = self.category,
			fg_color = DASHBOARD_OPTIONMENU_COLOR['background'],
			dropdown_fg_color = DASHBOARD_OPTIONMENU_COLOR['background'],
			button_color = DASHBOARD_OPTIONMENU_COLOR['background'],
			text_color = DASHBOARD_OPTIONMENU_COLOR['foreground'],
			dropdown_text_color = DASHBOARD_OPTIONMENU_COLOR['foreground'])
		self.dashboard_refresh_button = ctk.CTkButton(self.dashboard_control_frame,
			text = 'Refresh',
			corner_radius = DASHBOARD_BUTTON_CONFIG['corner'],
			hover = DASHBOARD_BUTTON_CONFIG['hover'],
			font = DASHBOARD_BUTTON_CONFIG['font'],
			fg_color = DASHBOARD_BUTTON_COLOR['background'],
			text_color = DASHBOARD_BUTTON_COLOR['foreground'],
			hover_color = DASHBOARD_BUTTON_COLOR['hover'])

		# -------------------------------------------------------------------------------------------

		self.dashboard_category_label.grid(
			row = 0,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady =10)
		self.dashboard_category_optionmenu.grid(
			row = 1,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady =10)
		self.dashboard_refresh_button.grid(
			row = 1,
			column = 1,
			# sticky = 'ew',
			padx = 10,
			pady = 10)

		# ----------------------------------------------------------------------------------------------

		# grand children frame
		self.dashboard_quantity_frame = ctk.CTkFrame(self.dashboard_details_frame,
			fg_color = DASHBOARD_DETAILS_FRAME_CONFIG['background'])
		self.dashboard_price_frame = ctk.CTkFrame(self.dashboard_details_frame,
			fg_color = DASHBOARD_DETAILS_FRAME_CONFIG['background'])
		# self.dashboard_quantity_frame = ctk.CTkFrame(self.dashboard_details_frame,
		# 	fg_color = DASHBOARD_DETAILS_FRAME_CONFIG['background'])
		# self.dashboard_quantity_frame = ctk.CTkFrame(self.dashboard_details_frame,
		# 	fg_color = DASHBOARD_DETAILS_FRAME_CONFIG['background'])

		# --------------------------------------------------------------------------------------------------

		self.dashboard_quantity_frame.grid(
			row = 0,
			column = 0,
			sticky = 'nsew',
			padx = 10,
			pady = 10)
		self.dashboard_price_frame.grid(
			row = 0,
			column = 1,
			sticky = 'nsew',
			padx = 10,
			pady = 10)

		# --------------------------------------------------------------------------------------------------

		self.dashboard_quantity_label = ctk.CTkLabel(self.dashboard_quantity_frame,
			text = 'Total Quantity',
			corner_radius = DASHBOARD_LABEL_CONFIG['corner'],
			font = DASHBOARD_LABEL_CONFIG['font'][0],
			fg_color = DASHBOARD_LABEL_COLOR['background'],
			text_color = DASHBOARD_LABEL_COLOR['foreground'])
		self.dashboard_quantity_val_label = ctk.CTkLabel(self.dashboard_quantity_frame,
			textvariable = self.quantity_val,
			corner_radius = DASHBOARD_LABEL_CONFIG['corner'],
			font = DASHBOARD_LABEL_CONFIG['font'][1],
			fg_color = DASHBOARD_LABEL_COLOR['background'],
			text_color = DASHBOARD_LABEL_COLOR['foreground'])
		self.dashboard_price_label = ctk.CTkLabel(self.dashboard_price_frame,
			text = 'Total Cost',
			corner_radius = DASHBOARD_LABEL_CONFIG['corner'],
			font = DASHBOARD_LABEL_CONFIG['font'][0],
			fg_color = DASHBOARD_LABEL_COLOR['background'],
			text_color = DASHBOARD_LABEL_COLOR['foreground'])
		self.dashboard_price_val_label = ctk.CTkLabel(self.dashboard_price_frame,
			textvariable = self.price_val,
			corner_radius = DASHBOARD_LABEL_CONFIG['corner'],
			font = DASHBOARD_LABEL_CONFIG['font'][1],
			fg_color = DASHBOARD_LABEL_COLOR['background'],
			text_color = DASHBOARD_LABEL_COLOR['foreground'])

		# ------------------------------------------------------------------------------------------------

		self.dashboard_quantity_label.pack(
			fill = 'x',
			padx = 4,
			pady = (4,2))
		self.dashboard_quantity_val_label.pack(
			fill = 'both',
			expand = True,
			padx = 4,
			pady = (2,4))
		self.dashboard_price_label.pack(
			fill = 'x',
			padx = 4,
			pady = (4,2))
		self.dashboard_price_val_label.pack(
			fill = 'both',
			expand = True,
			padx = 4,
			pady = (2,4))


class Product_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.product_control_frame = ctk.CTkFrame(self,
			fg_color = PRODUCT_FRAME_CONFIG['background'],
			border_width = PRODUCT_FRAME_CONFIG['border_width'],
			border_color = PRODUCT_FRAME_CONFIG['border_color'])
		self.product_control_frame.pack(
			side = 'top',
			fill = 'x', 
			padx = 4)

		self.product_details_frame = ctk.CTkFrame(self,
			fg_color = PRODUCT_FRAME_CONFIG['background'],
			border_width = PRODUCT_FRAME_CONFIG['border_width'],
			border_color = PRODUCT_FRAME_CONFIG['border_color'])
		self.product_details_frame.pack(
			fill = 'both', 
			expand= True,
			padx = 4,
			pady = 4)

		self.product_external_frame = ctk.CTkFrame(self,
			fg_color = PRODUCT_FRAME_CONFIG['background'],
			border_width = PRODUCT_FRAME_CONFIG['border_width'],
			border_color = PRODUCT_FRAME_CONFIG['border_color'])
		self.product_external_frame.pack(
			side = 'bottom',
			fill = 'x',
			padx = 4,)

		# child frame configuration
		self.product_control_frame.rowconfigure((0,1), weight = 1, uniform = 'a')
		self.product_control_frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')

		# -------------------------------------------------------------------------------------------

		# attribute declaration
		self.search_field = ctk.StringVar(value = PRODUCT_LIST[0][0])
		self.search_value = ctk.StringVar()
		p_LIST = []
		p_list = []
		for item in PRODUCT_LIST:
			p_LIST.append(item[0])
			p_list.append(item[1])

		# widgets configuration
		self.product_product_optionmenu = ctk.CTkOptionMenu(self.product_control_frame,
			values = p_LIST,
			corner_radius = PRODUCT_OPTIONMENU_CONFIG['corner'],
			font = PRODUCT_OPTIONMENU_CONFIG['font'],
			dropdown_font = PRODUCT_OPTIONMENU_CONFIG['font'],
			state = 'readonly',
			variable = self.search_field,
			fg_color = PRODUCT_OPTIONMENU_COLOR['background'],
			dropdown_fg_color = PRODUCT_OPTIONMENU_COLOR['background'],
			button_color = PRODUCT_OPTIONMENU_COLOR['background'],
			text_color = PRODUCT_OPTIONMENU_COLOR['foreground'],
			dropdown_text_color = PRODUCT_OPTIONMENU_COLOR['foreground'])
		self.product_search_entry = ctk.CTkEntry(self.product_control_frame,
			textvariable = self.search_value,
			corner_radius = PRODUCT_ENTRY_CONFIG['corner'],
			font = PRODUCT_ENTRY_CONFIG['font'],
			fg_color = PRODUCT_ENTRY_COLOR['background'])
		self.product_search_button = ctk.CTkButton(self.product_control_frame,
			text = 'Search',
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])
		self.product_refresh_button = ctk.CTkButton(self.product_control_frame,
			text = 'Refresh',
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])
		self.product_create_button = ctk.CTkButton(self.product_control_frame,
			text = 'Create',
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])
		self.product_update_button = ctk.CTkButton(self.product_control_frame,
			text = 'Update',
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])
		self.product_delete_button = ctk.CTkButton(self.product_control_frame,
			text = 'Delete',
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])

		# --------------------------------------------------------------------------------------------
		
		self.product_product_optionmenu.grid(
			row = 0,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.product_search_entry.grid(
			row = 0,
			column = 1,
			columnspan = 2,
			sticky = 'ew')
		self.product_search_button.grid(
			row = 0,
			column = 3,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.product_refresh_button.grid(
			row = 1,
			column = 0,
			# sticky = 'ew',
			padx = 10,
			pady = 10)
		self.product_create_button.grid(
			row = 1,
			column = 1,
			# sticky = 'ew',
			padx = (0,10),
			pady = 10)
		self.product_update_button.grid(
			row = 1,
			column = 2,
			# sticky = 'ew',
			pady = 10)
		self.product_delete_button.grid(
			row = 1,
			column = 3,
			# sticky = 'ew',
			padx = 10,
			pady = 10)

		# -------------------------------------------------------------------------------------------

		# table declaration
		self.product_table = ttk.Treeview(self.product_details_frame,
			columns = p_list,
			show = 'headings')
		self.product_table.heading(PRODUCT_LIST[0][1], 
			text = PRODUCT_LIST[0][0])
		self.product_table.column(PRODUCT_LIST[0][1], 
			width = PRODUCT_LIST[0][2], 
			anchor = PRODUCT_LIST[0][3])
		self.product_table.heading(PRODUCT_LIST[1][1], 
			text = PRODUCT_LIST[1][0])
		self.product_table.column(PRODUCT_LIST[1][1], 
			width = PRODUCT_LIST[1][2], 
			anchor = PRODUCT_LIST[1][3])
		self.product_table.heading(PRODUCT_LIST[2][1], 
			text = PRODUCT_LIST[2][0])
		self.product_table.column(PRODUCT_LIST[2][1], 
			width = PRODUCT_LIST[2][2], 
			anchor = PRODUCT_LIST[2][3])
		self.product_table.heading(PRODUCT_LIST[3][1], 
			text = PRODUCT_LIST[3][0])
		self.product_table.column(PRODUCT_LIST[3][1], 
			width = PRODUCT_LIST[3][2], 
			anchor = PRODUCT_LIST[3][3])
		self.product_table.heading(PRODUCT_LIST[4][1], 
			text = PRODUCT_LIST[4][0])
		self.product_table.column(PRODUCT_LIST[4][1], 
			width = PRODUCT_LIST[4][2], 
			anchor = PRODUCT_LIST[4][3])
		self.product_table.heading(PRODUCT_LIST[5][1], 
			text = PRODUCT_LIST[5][0])
		self.product_table.column(PRODUCT_LIST[5][1], 
			width = PRODUCT_LIST[5][2], 
			anchor = PRODUCT_LIST[5][3])
		self.product_table.heading(PRODUCT_LIST[6][1], 
			text = PRODUCT_LIST[6][0])
		self.product_table.column(PRODUCT_LIST[6][1], 
			width = PRODUCT_LIST[6][2], 
			anchor = PRODUCT_LIST[6][3])
		
		self.product_scrollbar = ctk.CTkScrollbar(
			self.product_details_frame,
			command = self.product_table.yview)
		self.product_table.configure(yscrollcommand = self.product_scrollbar.set)

		# -------------------------------------------------------------------------------------------
		
		self.product_table.place(
			relx = 0,
			rely = 0,
			relwidth = 0.99,
			relheight = 1,
			anchor = 'nw')
		self.product_scrollbar.place(
			relx = 1,
			rely = 0,
			relheight = 1,
			anchor = 'ne')

		# ---------------------------------------------------------------------------------------------

		self.product_export_button = ctk.CTkButton(self.product_external_frame, 
			text = 'Export', 
			corner_radius = PRODUCT_BUTTON_CONFIG['corner'],
			hover = PRODUCT_BUTTON_CONFIG['hover'],
			font = PRODUCT_BUTTON_CONFIG['font'],
			fg_color = PRODUCT_BUTTON_COLOR['background'],
			text_color = PRODUCT_BUTTON_COLOR['foreground'],
			hover_color = PRODUCT_BUTTON_COLOR['hover'])

		# ---------------------------------------------------------------------------------------------

		self.product_export_button.pack(
			side = 'right', 
			padx=10, 
			pady=10)


class Update_Page(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, fg_color = DISPLAY_FRAME_COLOR['page'])

		# child frame declaration
		self.update_frame = ctk.CTkFrame(self,
			fg_color = UPDATE_FRAME_CONFIG['background'],
			border_width = UPDATE_FRAME_CONFIG['border_width'],
			border_color = UPDATE_FRAME_CONFIG['border_color'])
		self.update_frame.place(
			relx = UPDATE_FRAME_POSITION[0], 
			rely = UPDATE_FRAME_POSITION[1], 
			relwidth = UPDATE_FRAME_POSITION[2], 
			relheight = UPDATE_FRAME_POSITION[3], 
			anchor = UPDATE_FRAME_POSITION[4])

		# child frame configuration
		self.update_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
		self.update_frame.columnconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')

		# ----------------------------------------------------------------------------------------

		# attribute declaration
		category_list = PRODUCT_CATEGORY_LIST
		self.id = ctk.StringVar(value = '')
		self.category = ctk.StringVar(value = '')
		self.name = ctk.StringVar(value = '')
		self.description = ctk.StringVar(value = '')
		self.quantity = ctk.StringVar(value = '')
		self.unit_price = ctk.StringVar(value = '')
		self.total_price = ctk.StringVar(value = '')

		# ----------------------------------------------------------------------------------------

		# widgets configuration
		self.update_id_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[0][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_id_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.id,
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_category_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[1][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_category_combobox = ctk.CTkComboBox(self.update_frame,
			values = category_list,
			corner_radius = UPDATE_OPTIONMENU_CONFIG['corner'],
			font = UPDATE_OPTIONMENU_CONFIG['font'],
			dropdown_font = UPDATE_OPTIONMENU_CONFIG['font'],
			variable = self.category,
			fg_color = UPDATE_OPTIONMENU_COLOR['background'],
			dropdown_fg_color = UPDATE_OPTIONMENU_COLOR['background'],
			button_color = PRODUCT_OPTIONMENU_COLOR['background'],
			button_hover_color = PRODUCT_OPTIONMENU_COLOR['hover'],
			text_color = UPDATE_OPTIONMENU_COLOR['foreground'],
			dropdown_text_color = UPDATE_OPTIONMENU_COLOR['foreground'])
		self.update_name_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[2][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_name_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.name,
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_description_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[3][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_description_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.description,
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_quantity_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[4][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_quantity_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.quantity,
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_unit_price_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[5][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_unit_price_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.unit_price,
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_total_price_label = ctk.CTkLabel(self.update_frame,
			text = PRODUCT_LIST[6][0],
			corner_radius = UPDATE_LABEL_CONFIG['corner'],
			font = UPDATE_LABEL_CONFIG['font'],
			fg_color = UPDATE_LABEL_COLOR['background'],
			text_color = UPDATE_LABEL_COLOR['foreground'])
		self.update_total_price_entry = ctk.CTkEntry(self.update_frame,
			textvariable = self.total_price,
			state = 'disabled',
			corner_radius = UPDATE_ENTRY_CONFIG['corner'],
			font = UPDATE_ENTRY_CONFIG['font'],
			fg_color = UPDATE_ENTRY_COLOR['background'])
		self.update_total_price_button = ctk.CTkButton(self.update_frame,
			text = 'Calculate',
			corner_radius = UPDATE_BUTTON_CONFIG['corner'],
			hover = UPDATE_BUTTON_CONFIG['hover'],
			font = UPDATE_BUTTON_CONFIG['font'],
			fg_color = UPDATE_BUTTON_COLOR['background'],
			text_color = UPDATE_BUTTON_COLOR['foreground'],
			hover_color = UPDATE_BUTTON_COLOR['hover'])

		self.update_create_button = ctk.CTkButton(self.update_frame, 
			text = 'Create Product',
			corner_radius = UPDATE_BUTTON_CONFIG['corner'],
			hover = UPDATE_BUTTON_CONFIG['hover'],
			font = UPDATE_BUTTON_CONFIG['font'],
			fg_color = UPDATE_BUTTON_COLOR['background'],
			text_color = UPDATE_BUTTON_COLOR['foreground'],
			hover_color = UPDATE_BUTTON_COLOR['hover'])
		self.update_update_button = ctk.CTkButton(self.update_frame, 
			text = 'Update Product',
			corner_radius = UPDATE_BUTTON_CONFIG['corner'],
			hover = UPDATE_BUTTON_CONFIG['hover'],
			font = UPDATE_BUTTON_CONFIG['font'],
			state = 'disabled',
			fg_color = UPDATE_BUTTON_COLOR['background'],
			text_color = UPDATE_BUTTON_COLOR['foreground'],
			hover_color = UPDATE_BUTTON_COLOR['hover'])

		# ----------------------------------------------------------------------------------------
		self.update_id_label.grid(
			row = 0,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (20,10))
		self.update_id_entry.grid(
			row = 0,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (20,10))
		self.update_category_label.grid(
			row = 0,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (20,10))
		self.update_category_combobox.grid(
			row = 0,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (20,10))
		self.update_name_label.grid(
			row = 1,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.update_name_entry.grid(
			row = 1,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (10,10))
		self.update_quantity_label.grid(
			row = 1,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (10,10))
		self.update_quantity_entry.grid(
			row = 1,
			column = 4,
			columnspan = 2,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))
		self.update_description_label.grid(
			row = 2,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.update_description_entry.grid(
			row = 2,
			column = 1,
			columnspan = 5,
			sticky = 'ew',
			padx = (10,20),
			pady = (10,10))
		self.update_unit_price_label.grid(
			row = 3,
			column = 0,
			sticky = 'e',
			padx = (10,5),
			pady = (10,10))
		self.update_unit_price_entry.grid(
			row = 3,
			column = 1,
			columnspan = 2,
			sticky = 'ew',
			padx = (10,10),
			pady = (10,10))
		self.update_total_price_label.grid(
			row = 3,
			column = 3,
			sticky = 'e',
			padx = (5,5),
			pady = (10,10))
		self.update_total_price_entry.grid(
			row = 3,
			column = 4,
			columnspan = 1,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))
		self.update_total_price_button.grid(
			row = 3,
			column = 5,
			columnspan = 1,
			sticky = 'ew',
			padx = (0,20),
			pady = (10,10))

		self.update_create_button.grid(
			row = 4,
			column = 1,
			columnspan = 2,
			padx = 10,
			pady = 10)
		self.update_update_button.grid(
			row = 4,
			column = 3,
			columnspan = 2,
			padx = 10,
			pady = 10)

