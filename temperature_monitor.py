#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO

#----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7(GPIO4).
#----------------------------------------------------------------

# Reads temperature from sensor and prints to stdout
# id is the id of the sensor

# Fan Pins
FAN = 17

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(FAN, GPIO.OUT)
	GPIO.output(FAN, GPIO.LOW)


def readSensor(id, min_temp=27):
	tfile = open("/sys/bus/w1/devices/"+str(id)+"/w1_slave")
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	#print ("Sensor: " + str(id)  + " - Current temperature : %0.3f C" % temperature)
	
	if(temperature >= min_temp):
		GPIO.output(FAN, GPIO.HIGH)
	else:
		GPIO.output(FAN, GPIO.LOW)
	return temperature


# Reads temperature from all sensors found in /sys/bus/w1/devices/
# starting with "28-...
def readSensors(min_temp=27):

	for file in os.listdir("/sys/bus/w1/devices/"):
		if (file.startswith("28-")):
			return readSensor(file, min_temp)


# read temperature every second for all connected sensors
def loop():
	while True:
		readSensors(27)
		time.sleep(1)
		

# Nothing to cleanup
def destroy():
	pass

# Main starts here
if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
	finally:
		GPIO.cleanup()
