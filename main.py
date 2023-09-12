import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox, filedialog
from settings import *
from defaults import *
from database import Database
from menu import Menu
from control import Control
from display import Display
from PIL import Image
import pandas as pd
import re

class IMS(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = WINDOW_COLOR['background'])

		# window configuration
		self.title(WINDOW_TITLE)
		self.set_window_size()
		self.mode = DEFAULT_WINDOW_APPEARANCE
		self.set_appearance()

		# ---------------------------------------------------------------------------------------------

		# child frame declaration
		self.main = Main(self)

		# ----------------------------------------------------------------------------------------------

		# window functions

		# bind escape function
		self.bind('<Escape>', lambda event: self.quit())

		# switch appearance functon
		self.main.menu.mode_button.configure(command = self.set_appearance)

		# switch fullscreen function
		self.main.display.settings_page.settings_titlebar_button.configure(command = self.set_titlebar)
		self.set_titlebar()

		# switch titlebar function
		self.main.display.settings_page.settings_fullscreen_button.configure(command = self.set_fullscreen)
		self.set_fullscreen()

		# ----------------------------------------------------------------------------------------------

		self.update()
		self.mainloop()

	def set_window_size(self):
		screen_width = int(self.winfo_screenwidth())
		screen_height = int(self.winfo_screenheight())
		win_width = int(screen_width * WINDOW_DISPLAY_RATIO['ratio'])
		win_height = int(screen_height * WINDOW_DISPLAY_RATIO['ratio'])
		pos_x = int((screen_width - win_width) / 2.0)
		pos_y = int((screen_height - win_height) / 2.0)
		self.geometry(f'{win_width}x{win_height}+{pos_x}+{pos_y}')
		self.minsize(WINDOW_DISPLAY_RATIO['minsize'][0],WINDOW_DISPLAY_RATIO['minsize'][1])

	def set_appearance(self):
		ctk.set_appearance_mode(self.mode)
		try:
			self.iconbitmap(WINDOW_ICON_PATH[self.mode])
		except:
			pass
		if self.mode == 'dark':
			self.mode = 'light'
		else:
			self.mode = 'dark'

	def set_fullscreen(self):
		if self.main.display.settings_page.fullscreen.get():
			self.state('zoomed')
		else:
			self.state('normal')

	def set_titlebar(self):
		if self.main.display.settings_page.titlebar.get():
			self.overrideredirect(True)
		else:
			self.overrideredirect(False)


class Main(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, border_width = 0, fg_color = WINDOW_COLOR['main'])

		# Main frame configuration
		self.pack(expand = True, fill = 'both')

		# ---------------------------------------------------------------------------------------------

		# child frame declaration
		self.menu = Menu(self)
		self.workbook = ctk.CTkFrame(self, fg_color = 'transparent')
		self.workbook.pack(expand = True, fill = 'both', padx = 4, pady = (2,4))
		self.control = Control(self.workbook)
		self.display = Display(self.workbook)

		# ---------------------------------------------------------------------------------------------

		# create database
		self.dbms = Database(DEFAULT_DATABASE)

		# ----------------------------------------------------------------------------------------------

		# animation attribute declaration
		self.control_frame_position = (
			CONTROL_FRAME_POSITION['initial'], 
			CONTROL_FRAME_POSITION['final'])
		self.display_frame_position = (
			DISPLAY_FRAME_POSITION['initial'], 
			DISPLAY_FRAME_POSITION['final'])
		self.animation_access = self.display.settings_page.animation
		self.selected_menu = ctk.StringVar(value = DEFAULT_MENU_BUTTON)
		self.menu_dict = {
			'profile': (self.control.profile, self.menu.profile_button),
			'product': (self.control.option, self.menu.product_button)
		}

		# animation
		self.menu.profile_button.configure(command = lambda: self.after(100, self.animate('profile')))
		self.menu.product_button.configure(command = lambda: self.after(100, self.animate('product')))
		
		# first run
		self.animate(DEFAULT_MENU_BUTTON)

		# ----------------------------------------------------------------------------------------------

		# page select attribute declaration
		self.selected_display = ctk.StringVar(value = 'dashboard')
		self.control_dict = {
			'user': (self.display.user_page, self.control.profile.user_button),
			'profile': (self.display.profile_page, self.control.profile.profile_button),
			'employee': (self.display.employee_page, self.control.profile.employee_button),
			'settings': (self.display.settings_page, self.control.profile.settings_button),
			'dashboard': (self.display.dashboard_page, self.control.option.dashboard_button),
			'product': (self.display.product_page, self.control.option.product_button),
			'update': (self.display.update_page, self.control.option.update_button)
		}

		# control indicator and page switch
		self.control.profile.user_button.configure(command = lambda: self.after(100, self.page_select('user')))
		self.control.profile.profile_button.configure(command = lambda: self.after(100, self.page_select('profile')))
		self.control.profile.employee_button.configure(command = lambda: self.after(100, self.page_select('employee')))
		self.control.profile.settings_button.configure(command = lambda: self.after(100, self.page_select('settings')))
		self.control.option.dashboard_button.configure(command = lambda: self.after(100, self.page_select('dashboard')))
		self.control.option.product_button.configure(command = lambda: self.after(100, self.page_select('product')))
		self.control.option.update_button.configure(command = lambda: self.after(100, self.page_select('update')))
		self.display.employee_page.employee_create_button.configure(command = lambda: self.after(100, self.page_select('user')))
		self.display.product_page.product_create_button.configure(command = lambda: self.after(100, self.page_select('update')))

		# first run
		self.page_select(DEFAULT_CONTROL_BUTTON)

		# -------------------------------------------------------------------------------------------------

		# table attribute declaration
		self.employee_data = (
			self.display.user_page.user, 
			self.display.user_page.username, 
			self.display.user_page.first,  
			self.display.user_page.last, 
			self.display.user_page.access, 
			self.display.user_page.email, 
			self.display.user_page.phone,
			self.display.user_page.password)
		self.product_data = (
			self.display.update_page.id, 
			self.display.update_page.category, 
			self.display.update_page.name,  
			self.display.update_page.description, 
			self.display.update_page.quantity, 
			self.display.update_page.unit_price, 
			self.display.update_page.total_price)

		# show entry in employee database
		self.show_entry('employee', 1)
		# self.show_entry('product', 1)

		# refresh entry in employee/product database --------------------------
		self.display.employee_page.employee_refresh_button.configure(command = lambda: self.after(100, self.show_entry('employee', 1)))
		self.display.product_page.product_refresh_button.configure(command = lambda: self.after(100, self.show_entry('product', 1)))

		# search entry in employee/product database ---------------------------
		self.display.employee_page.employee_search_button.configure(command = lambda: self.after(100, self.search_entry('employee')))
		self.display.product_page.product_search_button.configure(command = lambda: self.after(100, self.search_entry('product')))

		# create entry in employee/product database ---------------------------
		self.display.user_page.user_create_button.configure(command = lambda: self.after(100, self.create_entry('employee')))
		self.display.update_page.update_create_button.configure(command = lambda: self.after(100, self.create_entry('product')))

		# update entry in employee/product database ---------------------------
		self.display.user_page.user_update_button.configure(command = lambda: self.after(100, self.update_entry('employee')))
		self.display.employee_page.employee_update_button.configure(command = lambda: self.after(100, self.update_set('employee')))
		self.display.update_page.update_update_button.configure(command = lambda: self.after(100, self.update_entry('product')))
		self.display.product_page.product_update_button.configure(command = lambda: self.after(100, self.update_set('product')))

		# delete entry in employee/product database ----------------------------
		self.display.employee_page.employee_delete_button.configure(command = lambda: self.after(100, self.delete_entry('employee')))
		self.display.product_page.product_delete_button.configure(command = lambda: self.after(100, self.delete_entry('product')))

		# ---------------------------------------------------------------------------------------------------

		# login attribute declaration
		self.access_dict = {
			'read': (
				self.control.profile.user_button,
				self.control.profile.employee_button,
				self.control.option.update_button,
				self.display.product_page.product_create_button,
				self.display.product_page.product_update_button,
				self.display.product_page.product_delete_button),
			'write': (
				self.control.profile.user_button,
				self.control.profile.employee_button),
			'admin': (),
			'denied': (
				self.control.profile.user_button,
				self.control.profile.employee_button,
				self.control.option.dashboard_button,
				self.control.option.product_button,
				self.control.option.update_button),
		}
		self.selected_access = ctk.StringVar(value = 'denied')
		self.selected_status = ctk.StringVar(value = 'logged out')

		# user login access
		self.display.profile_page.profile_login_button.configure(command = lambda: self.login_user())
		self.display.profile_page.profile_logout_button.configure(command = lambda: self.login_set('logged out'))

		# run
		self.login_set(DEFAULT_LOG_STATUS[0], DEFAULT_LOG_STATUS[1])

		# check user
		if self.show_entry('user', 0) == []:
			self.login_set('logged in', 'admin')
			self.display.user_page.access.set('admin')

		# ----------------------------------------------------------------------------------------------------

		# dashboard setup
		self.display.dashboard_page.dashboard_category_optionmenu.configure(command = lambda event: self.dashboard_category_query('product'))
		self.display.dashboard_page.dashboard_refresh_button.configure(command = lambda: self.dashboard_category_query('product'))

		# first run
		self.dashboard_category_query('product')

		# ----------------------------------------------------------------------------------------------------

		# export file
		self.display.product_page.product_export_button.configure(command = lambda: self.export_file('product'))

		# ---------------------------------------------------------------------------------------------------

	def animate(self, arg):
		if self.animation_access.get() == True:
			if self.selected_menu.get() == arg:
				if self.control.initial <= self.control_frame_position[0]:
					self.menu_dict[self.selected_menu.get()][0].pack(expand = True, fill = 'both')
					self.go_forward()
				elif self.control.initial >= self.control_frame_position[1]:
					self.go_backward()
					self.menu_dict[self.selected_menu.get()][0].pack_forget()
			else:
				if self.control.initial <= self.control_frame_position[0]:
					self.selected_menu.set(arg)
					self.menu_dict[self.selected_menu.get()][0].pack(expand = True, fill = 'both')
					self.go_forward()
				elif self.control.initial >= self.control_frame_position[1]:
					self.menu_dict[self.selected_menu.get()][0].pack_forget()
					self.selected_menu.set(arg)
					self.menu_dict[self.selected_menu.get()][0].pack(expand = True, fill = 'both')
		else:
			self.control.place(relx = self.control.final, rely = 0, relwidth = self.control.width, relheight = 1)
			self.menu_dict[self.selected_menu.get()][0].pack_forget()
			self.selected_menu.set(arg)
			self.menu_dict[self.selected_menu.get()][0].pack(expand = True, fill = 'both')
			self.display.place(relx = self.display.final, rely = 0, relwidth = abs(1.0-self.display.final), relheight = 1)
		self.menu.indicator(self.menu_dict[self.selected_menu.get()][1], self.animation_access.get())
	
	def go_forward(self):
		self.control.place(relx = self.control_frame_position[1], rely = 0, relwidth = self.control.width, relheight = 1)
		self.display.place(relx = self.display_frame_position[1], rely = 0, relwidth = abs(1.0-self.display_frame_position[1]), relheight = 1)
		self.control.initial = self.control_frame_position[1]
		self.display.initial = self.display_frame_position[1]

	def go_backward(self):
		self.control.place(relx = self.control_frame_position[0], rely = 0, relwidth = self.control.width, relheight = 1)
		self.display.place(relx = self.display_frame_position[0], rely = 0, relwidth = abs(1.0-self.display_frame_position[0]), relheight = 1)
		self.control.initial = self.control_frame_position[0]
		self.display.initial = self.display_frame_position[0]

	def login_user(self):
		username = self.display.profile_page.username.get()
		password = self.display.profile_page.password.get()
		for i,item in enumerate(self.show_entry('user', 0)):
			if username in item[1] and password == item[2]:
				self.selected_access.set(item[3])
				self.selected_status.set('logged in')
				self.login_set('logged in', item[3])
				self.display.profile_page.username.set('')
				self.display.profile_page.password.set('')
				try:
					for item in self.show_entry('employee', 0):
						if item[1] == username:
							value = item
					self.display.profile_page.id.set(value[0])
				except:
					value = ['*','*','*','*','*','*','*']
				self.display.profile_page.id.set(value[0])
				self.display.profile_page.user.set(value[1])
				self.display.profile_page.name.set(value[2] + ' ' + value[3])
				self.display.profile_page.access.set(value[4])
				self.display.profile_page.email.set(value[5])
				self.display.profile_page.phone.set(value[6])
				self.show_entry('employee', 1)
				return
		messagebox.showerror('Error', 'wrong username / password')

	def login_set(self, arg1 = 'logged out', arg2 = 'denied'):
		if arg1 == 'logged out':
			for item in self.access_dict['denied']:
				item.configure(state = 'disabled')
			self.selected_access.set('denied')
			self.selected_status.set('logged out')
			self.display.profile_page.profile_login_button.configure(state = 'normal')
			self.display.profile_page.profile_login_frame.place(
				relx = PROFILE_LOGIN_FRAME_POSITION[0], 
				rely = PROFILE_LOGIN_FRAME_POSITION[1], 
				relwidth = PROFILE_LOGIN_FRAME_POSITION[2], 
				relheight = PROFILE_LOGIN_FRAME_POSITION[3], 
				anchor = PROFILE_LOGIN_FRAME_POSITION[4])
			self.display.profile_page.profile_user_frame.place_forget()
		elif arg1 == 'logged in':
			for item in self.access_dict['denied']:
				item.configure(state = 'normal')
			for item in self.access_dict[arg2]:
				item.configure(state = 'disabled')
			self.display.profile_page.profile_login_button.configure(state = 'disabled')
			self.display.profile_page.profile_login_frame.place_forget()
			self.display.profile_page.profile_user_frame.place(
				relx = PROFILE_DETAILS_FRAME_POSITION[0], 
				rely = PROFILE_DETAILS_FRAME_POSITION[1], 
				relwidth = PROFILE_DETAILS_FRAME_POSITION[2], 
				relheight = PROFILE_DETAILS_FRAME_POSITION[3], 
				anchor = PROFILE_DETAILS_FRAME_POSITION[4])

	def page_select(self, page):
		if self.selected_display.get() != page:
			self.control_dict[self.selected_display.get()][0].pack_forget()
		self.selected_display.set(page)
		self.control_dict[self.selected_display.get()][0].pack(expand = True, fill = 'both')
		self.control.indicator(self.control_dict[self.selected_display.get()][1])

	def show_entry(self, arg, flag = None):
		datalist = []
		category1 = []
		category2 = ['All']
		self.dbms.create_connection()

		if arg == 'employee':
			self.display.employee_page.search_value.set('')
			self.display.employee_page.employee_table.delete(*self.display.employee_page.employee_table.get_children())
			for item in self.dbms.select_entry(arg):
				if flag == 1:
					self.display.employee_page.employee_table.insert('', 'end', values = item)
				datalist.append(item)
		elif arg == 'user':
			for item in self.dbms.select_entry(arg):
				datalist.append(item)
		elif arg == 'product':
			self.display.product_page.search_value.set('')
			self.display.product_page.product_table.delete(*self.display.product_page.product_table.get_children())
			for item in self.dbms.select_entry(arg):
				if flag == 1:
					if item[1] not in category1:
						category1.append(item[1])
						category2.append(item[1])
						self.display.update_page.update_category_combobox.configure(values = category1)
						self.display.dashboard_page.dashboard_category_optionmenu.configure(values = category2)
					self.display.product_page.product_table.insert('', 'end', values = item)
				datalist.append(item)

		self.dbms.close_connection()
		if flag == 0:
			return datalist

	def search_entry(self, arg):
		datalist = []
		if arg == 'employee':
			value = self.display.employee_page.search_value.get()
			for i, item in enumerate(EMPLOYEE_LIST):
				if item[0] == self.display.employee_page.search_field.get():
					field = i
		elif arg == 'product':
			value = self.display.product_page.search_value.get()
			for i, item in enumerate(PRODUCT_LIST):
				if item[0] == self.display.product_page.search_field.get():
					field = i

		if value != '':
			for item in self.show_entry(arg, 0):
				if re.search(value, item[field]) != None:
					if arg == 'employee':
						self.display.employee_page.employee_table.insert('', 'end', values = item)
					elif arg == 'product':
						self.display.product_page.product_table.insert('', 'end', values = item)
			if arg == 'employee':
				self.display.employee_page.search_value.set(value)
			elif arg == 'product':
				self.display.product_page.search_value.set(value)
			return
		else:
			messagebox.showerror('Error', 'Enter search query')
		self.show_entry(arg, 1)
		
	def create_entry(self, arg):
		datalist = []
		validation = ''
		if arg == 'employee':
			for item in self.employee_data:
				datalist.append(item.get())
				item.set('')
			try:
				validation = int(datalist[0])
				datalist[0] = 'ID' + datalist[0]
			except ValueError:
				pass
		elif arg == 'product':
			for item in self.product_data:
				datalist.append(item.get())
				item.set('')
			try:
				validation = int(datalist[0])
				datalist[0] = 'ID' + datalist[0]
			except ValueError:
				pass

		if '' in datalist:
			messagebox.showerror('Error', 'Empty Field')
			return
		for item in self.show_entry(arg, 0):
			if datalist[0] == item[0]:
				messagebox.showerror('Error', 'Entry Id Already present')
				return
			elif datalist[1] == item[1] and arg == 'employee':
				messagebox.showerror('Error', 'username Already present')
				return

		self.dbms.create_connection()
		self.dbms.create_entry(arg, tuple(datalist))
		self.dbms.close_connection()
		self.show_entry(arg, 1)
		messagebox.showinfo('Success', 'Entry Successfully Created')

	def update_set(self, arg):
		if arg == 'employee':
			self.page_select('user')
			self.display.user_page.user_update_button.configure(state = 'normal')
			self.display.user_page.user_create_button.configure(state = 'disabled')
			if self.display.employee_page.employee_table.selection() != ():
				value = self.display.employee_page.employee_table.item(
							self.display.employee_page.employee_table.selection()[0])
				for item in self.show_entry('user', 0):
					if value['values'][0] == item[0]:
						value['values'].append(item[2])
				for i, item in enumerate(self.employee_data):
					item.set(value['values'][i])
		elif arg == 'product':
			self.page_select('update')
			self.display.update_page.update_update_button.configure(state = 'normal')
			self.display.update_page.update_create_button.configure(state = 'disabled')
			if self.display.product_page.product_table.selection() != ():
				value = self.display.product_page.product_table.item(
							self.display.product_page.product_table.selection()[0])
				for i, item in enumerate(self.product_data):
					item.set(value['values'][i])
				self.product_data[-1].set('')

	def update_entry(self, arg):
		datalist = []
		flag = 0
		if arg == 'employee':
			self.display.user_page.user_update_button.configure(state = 'disabled')
			self.display.user_page.user_create_button.configure(state = 'normal')
			for item in self.employee_data:
				datalist.append(item.get())
				item.set('')
		elif arg == 'product':
			self.display.update_page.update_update_button.configure(state = 'disabled')
			self.display.update_page.update_create_button.configure(state = 'normal')
			for item in self.product_data:
				datalist.append(item.get())
				item.set('')

		if '' in datalist:
			messagebox.showerror('Error', 'Empty Field')
			return
		for item in self.show_entry(arg, 0):
			if datalist[0] == item[0]:
				flag = 1		
		
		if flag == 1:
			self.dbms.create_connection()
			self.dbms.update_entry(arg, datalist)
			self.dbms.close_connection()
			messagebox.showinfo('Success', 'Entry Successfully Updated')
		else:
			messagebox.showerror('Error', 'Entry Id not found')
		self.show_entry(arg, 1)

	def delete_entry(self, arg):
		datalist = []
		if arg == 'employee':
			if self.display.employee_page.employee_table.selection() != ():
				for selected_item in self.display.employee_page.employee_table.selection():
					item = self.display.employee_page.employee_table.item(selected_item)
					datalist.append(item['values'][0])
			else:
				messagebox.showerror('Error', 'Select Entry')
				return
		elif arg == 'product':
			if self.display.product_page.product_table.selection() != ():
				for selected_item in self.display.product_page.product_table.selection():
					item = self.display.product_page.product_table.item(selected_item)
					datalist.append(item['values'][0])
			else:
				messagebox.showerror('Error', 'Select Entry')
				return

		self.dbms.create_connection()
		self.dbms.delete_entry(arg, datalist)
		self.dbms.close_connection()
		messagebox.showinfo('Success', 'Entry Successfully Deleted')
		self.show_entry(arg, 1)

	def dashboard_category_query(self, arg):
		category = self.display.dashboard_page.category.get()
		datalist = self.show_entry(arg, 0)
		quantity = 0
		price = 0
		for item in datalist:
			if item[1] == category or category == 'All':
				quantity += int(item[4])
				price += float(item[6])

		self.display.dashboard_page.quantity_val.set(str(quantity))
		self.display.dashboard_page.price_val.set(str(price))
		self.show_entry(arg, 1)

	def export_file(self, arg):
		datalist = []
		columns = []
		if arg == 'product':
			for item in self.display.product_page.product_table.get_children():
				datalist.append(self.display.product_page.product_table.item(item)['values'])
			for item in PRODUCT_LIST:
				columns.append(item[0])

		file = (('xlsx', '*.xlsx'), ('csv', '*.csv'))
		path = filedialog.asksaveasfilename(
			initialdir = '/',
			title = 'save file',
			filetypes = file,
			defaultextension = file)
		df = pd.DataFrame(data = datalist, columns = columns)
		try:
			if re.search(r'.xlsx', path) != None:
				df.to_excel(path, index = False)
			elif re.search(r'.csv', path) != None:
				df.to_csv(path, index = False)
		except Exception as e:
			messagebox.showerror('Error', e)



if __name__ == '__main__':
	IMS()

