#!/usr/bin/env python
import ADC0832
import RPi.GPIO as GPIO
import time

MotorPin_A = 5
MotorPin_B = 6

def motorStop():
	GPIO.output(MotorPin_A, GPIO.HIGH)
	GPIO.output(MotorPin_B, GPIO.HIGH)

def init():
	ADC0832.setup()
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motorStop()
	
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
			
def destroy():
	motorStop()
	GPIO.cleanup() 
	ADC0832.destroy()

def loop():
	while True:
		res = ADC0832.getResult()
		moisture = 255 - res
		print ('analog value: %03d  moisture: %d' %(res, moisture))
		time.sleep(1)
		
		if(moisture < 50):
			motor(1,0)
		else:
			motor(0,0)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		destroy()
		print ('The end !')
