from tkinter import messagebox
from tkinter import ttk
from defaults import *
import sqlite3

class Database():
	def __init__(self, dbms_name):

		# attribute declaration
		self.database = dbms_name
		self.conn = None
		self.c = None

		# creating connection with database
		self.create_connection()

		if self.conn != None:
			# creating tables
			self.create_table()
			# closing connection to database
			self.close_connection()
		else:
			messagebox.showerror('Error', 'Failed to create connection with the database.')

	def create_connection(self):
		try:
			self.conn = sqlite3.connect(self.database, timeout = 1)
			self.c = self.conn.cursor()
		except Exception as e:
			messagebox.showerror('Error', e)

	def create_table(self):
		try:
			self.c.execute("""
				CREATE TABLE IF NOT EXISTS employee (
					eid text PRIMARY KEY,
					username text NOT NULL UNIQUE,
					first_name text,
					last_name text,
					access text NOT NULL,
					email_id text NOT NULL,
					phone_no text
				)
			""")
			self.c.execute("""
				CREATE TABLE IF NOT EXISTS user (
					eid text PRIMARY KEY,
					username text UNIQUE,
					password text,
					access text
				)
			""")
			self.c.execute("""
				CREATE TABLE IF NOT EXISTS product (
					pid text PRIMARY KEY,
					category text NOT NULL,
					product_name text NOT NULL,
					description text,
					quantity text NOT NULL,
					unit_price text,
					total_price text
				)
			""")
			self.conn.commit()
		except Exception as e:
			messagebox.showerror('Error', e)

	def close_connection(self):
		try:
			self.conn.commit()
			self.conn.close()
		except Exception as e:
			messagebox.showerror('Error', e)

	def create_entry(self, table, data):
		try:
			if table == 'employee':
				self.c.execute("""
					INSERT INTO employee (
					eid, 
					username,
					first_name,
					last_name,
					access,
					email_id,
					phone_no
					)
					VALUES (?,?,?,?,?,?,?)
				""", data[0:7])
				self.c.execute("""
					INSERT INTO user (
					eid, 
					username,
					password,
					access
					)
					VALUES (?,?,?,?)
				""", (data[0], data[1], data[7], data[4]))
			elif table == 'product':
				self.c.execute("""
					INSERT INTO product (
					pid, 
					category,
					product_name,
					description,
					quantity,
					unit_price,
					total_price
					)
					VALUES (?,?,?,?,?,?,?)
				""", data)
			self.conn.commit()
		except Exception as e:
			messagebox.showerror('Error', e)

	def select_entry(self, table):
		try:
			if table == 'employee':
				self.c.execute("""
					SELECT * FROM employee
				""")
			elif table == 'user':
				self.c.execute("""
					SELECT * FROM user
				""")
			elif table == 'product':
				self.c.execute("""
					SELECT * FROM product
				""")
			return self.c.fetchall()
		except Exception as e:
			messagebox.showerror('Error', e)

	def update_entry(self, table, data):
		try:
			if table == 'employee':
				self.c.execute("""
					UPDATE employee 
					SET 
					username = ?,
					first_name = ?,
					last_name = ?,
					access = ?,
					email_id = ?,
					phone_no = ?
					WHERE eid = ?
				""", (data[1], 
					data[2], 
					data[3], 
					data[4], 
					data[5], 
					data[6], 
					data[0]))
				self.c.execute("""
					UPDATE user 
					SET 
					username = ?,
					password = ?,
					access = ?
					WHERE eid = ?
				""", (data[1], data[7], data[4], data[0]))
			if table == 'product':
				self.c.execute("""
					UPDATE product 
					SET 
					category = ?,
					product_name = ?,
					description = ?,
					quantity = ?,
					unit_price = ?,
					total_price = ?
					WHERE pid = ?
				""", (data[1], 
					data[2], 
					data[3], 
					data[4], 
					data[5], 
					data[6], 
					data[0]))
			self.conn.commit()
		except Exception as e:
			messagebox.showerror('Error', e)

	def delete_entry(self, table, data):
		try:
			if table == 'employee':
				for item in data:
					self.c.execute("""
						DELETE FROM employee 
						WHERE eid = ?
					""", (item,))
					self.c.execute("""
						DELETE FROM user 
						WHERE eid = ?
					""", (item,))
			elif table == 'product':
				for item in data:
					self.c.execute("""
						DELETE FROM product 
						WHERE pid = ?
					""", (item,))
			self.conn.commit()
		except Exception as e:
			messagebox.showerror('Error', e)