#!/usr/bin/python3
from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		self.label1 = Label (self, text="Welcome to my Window!")
		self.label1.grid(row=0, column=0, sticky=W)
		
		self.button1 = Button (self, text="Click me", command=self.display)
		self.button1.grid(row=1, column=0, sticky=W)
		
	def display(self):
		print("The button in the Window was clicked.")

root = Tk()
root.title('This is a test window')
root.geometry('800x400')

app = Application(root)
app.mainloop()
