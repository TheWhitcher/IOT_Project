#!/usr/bin/python3
from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		# Create Title Label
		self.titleLabel = Label (self, text="Welcome to the Greenhouse!")
		self.titleLabel.grid(row=0, column=0, sticky=W)
		
		# Create Temperature labels
		self.tempLabel = Label (self, text="Temperature:")
		self.tempLabel.grid(row=2, column=0)
		
		self.tempRead = Label (self, text="Place Holder")
		self.tempRead.grid(row=2, column=1)


		
		self.label4 = Label (self, text="Fan")
		self.label4.grid(row=2, column=2, sticky=W)

		self.button1 = Button (self, text="Off",bg="red", command=self.btn1)
		self.button1.grid(row=2, column=3, sticky=W)

		# Create Humidity Labels
		self.humidLabel = Label (self, text="Humidity:")
		self.humidLabel.grid(row=3, column=0, sticky=W)

		self.humidRead = Label (self, text="Place Holder")
		self.humidRead.grid(row=3, column=1, sticky=W)

		self.label7 = Label (self, text="Watering System")
		self.label7.grid(row=3, column=2, sticky=W)

		self.button2 = Button (self, text="Off",bg="red", command=self.btn2)
		self.button2.grid(row=3, column=3, sticky=W)

		# Light Labels
		self.lightLabel = Label (self, text="Light:")
		self.lightLabel.grid(row=4, column=0, sticky=W)

		self.lightRead = Label (self, text="Place Holder")
		self.lightRead.grid(row=4, column=1, sticky=W)

		self.label10 = Label (self, text="Lighting System")
		self.label10.grid(row=4, column=2, sticky=W)

		self.button3 = Button (self, text="Off",bg="red", command=self.btn3)
		self.button3.grid(row=4, column=3, sticky=W)
		
	# Load Preset 1
	def btn1(self):
		if self.button1["bg"] == "red":
			self.button1["bg"] = "green"
			self.button1.config(text="On")
		else:
			self.button1["bg"] = "red"
			self.button1.config(text="Off")

	# Load Preset 2
	def btn2(self):
		if self.button2["bg"] == "red":
			self.button2["bg"] = "green"
			self.button2.config(text="On")
		else:
			self.button2["bg"] = "red"
			self.button2.config(text="Off")
			
	# Load Preset 3
	def btn3(self):
		if self.button3["bg"] == "red":
			self.button3["bg"] = "green"
			self.button3.config(text="On")
		else:
			self.button3["bg"] = "red"
			self.button3.config(text="Off")
