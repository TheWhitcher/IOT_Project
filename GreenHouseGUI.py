#!/usr/bin/python3
from tkinter import *
import soil_moisture_monitor
import temperature_monitor
import uv_light_monitor


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.label1 = Label (self, text="Welcome to the Greenhouse!")
		self.label1.grid(row=0, column=0, sticky=W)

		self.label2 = Label (self, text="Temperature: ")
		self.label2.grid(row=2, column=0, sticky=W)

		self.label3 = Label (self, text="Place Holder")
		self.label3.grid(row=2, column=1, sticky=W)

		self.label4 = Label (self, text="Fan")
		self.label4.grid(row=2, column=2, sticky=W)

		self.button1 = Button (self, text="Off",bg="red", command=self.btn1)
		self.button1.grid(row=2, column=3, sticky=W)

		self.label5 = Label (self, text="Humidity: ")
		self.label5.grid(row=3, column=0, sticky=W)

		self.label6 = Label (self, text="Place Holder")
		self.label6.grid(row=3, column=1, sticky=W)

		self.label7 = Label (self, text="Watering System")
		self.label7.grid(row=3, column=2, sticky=W)

		self.button2 = Button (self, text="Off",bg="red", command=self.btn2)
		self.button2.grid(row=3, column=3, sticky=W)

		self.label8 = Label (self, text="Light: ")
		self.label8.grid(row=4, column=0, sticky=W)

		self.label9 = Label (self, text="Place Holder")
		self.label9.grid(row=4, column=1, sticky=W)

		self.label10 = Label (self, text="Lighting System")
		self.label10.grid(row=4, column=2, sticky=W)

		self.button3 = Button (self, text="Off",bg="red", command=self.btn3)
		self.button3.grid(row=4, column=3, sticky=W)

	def display(self):
		print("Click!")

	def btn1(self):
		if self.button1["bg"] == "red":
			self.button1["bg"] = "green"
			self.button1.config(text="On")
		else:
			self.button1["bg"] = "red"
			self.button1.config(text="Off")

	def btn2(self):
		if self.button2["bg"] == "red":
			self.button2["bg"] = "green"
			self.button2.config(text="On")
		else:
			self.button2["bg"] = "red"
			self.button2.config(text="Off")

	def btn3(self):
		if self.button3["bg"] == "red":
			self.button3["bg"] = "green"
			self.button3.config(text="On")
		else:
			self.button3["bg"] = "red"
			self.button3.config(text="Off")

def setup():
	soil_moisture_monitor.setup()
	temperature_monitor.setup()
	uv_light_monitor.setup()

def loop():
	min_moisture = 50
	min_temp = 27
	min_uv = 50
	soil_moisture_monitor.readSensor(min_moisture)
	temperature_monitor.readSensor(min_temp)
	uv_light_monitor.readSensor(min_uv)

def destroy():
	soil_moisture_monitor.destroy()
	temperature_monitor.destroy()
	uv_light_monitor.destroy()

root = Tk()
root.title('Greenhouse GUI')
root.geometry('400x100')

app = Application(root)
app.mainloop()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
		print ('The end !')
	finally:
		destroy()