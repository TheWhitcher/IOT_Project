# Main GreenHouse Project
from tkinter import *
import os
import GreenHouseGUI
import temperature_monitor
import uv_light_monitor
import soil_moisture_monitor
import time

# Define what happens when the window is closed
def on_closing():
	# Send Ctrl+C signal to terminate the script
	try:
		print("GoodBye")
		destroy()
	finally:
		os._exit(0)
    
def setup():
	# Setup Sensors
	soil_moisture_monitor.setup()
	temperature_monitor.setup()
	uv_light_monitor.setup()
	
	# Setup GUI
	global app
	root=Tk()
	root.title('Greenhouse GUI')
	root.geometry('465x125')
	app = GreenHouseGUI.Application(root)
	
    # Bind the close event to the on_close() function	
	root.protocol("WM_DELETE_WINDOW", on_closing)

def loop():
	while True:
		# Default values
		min_moisture = 50
		min_temp = 27
		min_uv = 50
		
		# Get Sensor readings
		moisture = soil_moisture_monitor.readSensor(min_moisture)
		temperature = temperature_monitor.readSensors(min_temp)
		light = uv_light_monitor.readSensor(min_uv)
		
		# Update GUI Labels
		app.tempRead.config(text=str(temperature))
		app.humidRead.config(text=str(moisture))
		app.lightRead.config(text=str(light))
		
		# Update GUI
		app.update_idletasks()
		app.update()
		
		print("Temp:" + str(temperature) + "  Humidity:" + str(moisture) + "   Light:" + str(light))
            
		time.sleep(1)
	
def destroy():
	# Runs GPIO.cleanup
	soil_moisture_monitor.destroy()
	temperature_monitor.destroy()
	uv_light_monitor.destroy()
	
if __name__ == '__main__':
	setup()
try:
	loop()
except KeyboardInterrupt: 
	destroy()
	print ('The end !')
finally:
	destroy()
