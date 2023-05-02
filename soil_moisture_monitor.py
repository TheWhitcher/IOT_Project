#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Motor Pins
MotorPin_A = 5
MotorPin_B = 6

# Soil Moisture Pins
ADC_CS = 24
ADC_CLK = 23
ADC_DIO = 18

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ADC_CS, GPIO.OUT)
	GPIO.setup(ADC_CLK, GPIO.OUT)
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motorStop()

def destroy():
	motorStop()
	GPIO.cleanup()

def motorStop():
	GPIO.output(MotorPin_A, GPIO.HIGH)
	GPIO.output(MotorPin_B, GPIO.HIGH)

def getResult(): # ADC0832.py
	GPIO.setup(ADC_DIO, GPIO.OUT)
	GPIO.output(ADC_CS, 0)

	GPIO.output(ADC_CLK, 0)
	GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
	GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
	GPIO.output(ADC_CLK, 0)

	GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
	GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
	GPIO.output(ADC_CLK, 0)

	GPIO.output(ADC_DIO, 0);  time.sleep(0.000002)

	GPIO.output(ADC_CLK, 1)
	GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
	GPIO.output(ADC_CLK, 0)
	GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)

	dat1 = 0
	for i in range(0, 8):
		GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
		GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)
		GPIO.setup(ADC_DIO, GPIO.IN)
		dat1 = dat1 << 1 | GPIO.input(ADC_DIO)  # or ?
	
	dat2 = 0
	for i in range(0, 8):
		dat2 = dat2 | GPIO.input(ADC_DIO) << i
		GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
		GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)
	
	GPIO.output(ADC_CS, 1)
	GPIO.setup(ADC_DIO, GPIO.OUT)

	if dat1 == dat2:
		return dat1
	else:
		return 0
	
def motor(status, direction):
	if status == 0: # stop
		motorStop()
	else:
		if direction == 1:
			GPIO.output(MotorPin_A, GPIO.HIGH)
			GPIO.output(MotorPin_B, GPIO.LOW)
		else:
			GPIO.output(MotorPin_A, GPIO.LOW)
			GPIO.output(MotorPin_B, GPIO.HIGH)

def readSensor(min_moisture=100):
	res = getResult()
	moisture = 255 - res
	#print ('analog value: %03d  moisture: %d' %(res, moisture))
		
	if(moisture < min_moisture):
		motor(1,0)
	elif(moisture > min_moisture):
		motor(0,0)
		
	return moisture

def loop():
	while True:
		readSensor(150)
		time.sleep(0.5)

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt: 
		destroy()
		print ('The end !')
	finally:
		destroy()
