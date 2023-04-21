#!/usr/bin/python3
from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		self.label1 = Label (self, text="Welcome to the Greenhouse!")
		self.label1.grid(row=0, column=0, sticky=W)
		
		self.label1 = Label (self, text="Temperature: ")
		self.label1.grid(row=2, column=0, sticky=W)

		self.label1 = Label (self, text="Place Holder")
		self.label1.grid(row=2, column=1, sticky=W)

		self.label1 = Label (self, text="Fan")
		self.label1.grid(row=2, column=2, sticky=W)

		self.button1 = Button (self, text="On/Off", command=self.display)
		self.button1.grid(row=2, column=3, sticky=W)

		self.label1 = Label (self, text="Humidity: ")
		self.label1.grid(row=3, column=0, sticky=W)

		self.label1 = Label (self, text="Place Holder")
		self.label1.grid(row=3, column=1, sticky=W)

		self.label1 = Label (self, text="Watering System")
		self.label1.grid(row=3, column=2, sticky=W)

		self.button1 = Button (self, text="On/Off", command=self.display)
		self.button1.grid(row=3, column=3, sticky=W)

		self.label1 = Label (self, text="Light: ")
		self.label1.grid(row=4, column=0, sticky=W)

		self.label1 = Label (self, text="Place Holder")
		self.label1.grid(row=4, column=1, sticky=W)

		self.label1 = Label (self, text="Lighting System")
		self.label1.grid(row=4, column=2, sticky=W)

		self.button1 = Button (self, text="On/Off", command=self.display)
		self.button1.grid(row=4, column=3, sticky=W)

	def display(self):
		print("The button in the Window was clicked.")

root = Tk()
root.title('Greenhouse GUI')
root.geometry('400x100')

app = Application(root)
app.mainloop()
