#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

LED = 25

def init():
	ADC0832.setup()
	GPIO.setup(LED, GPIO.OUT)

def loop():
	while True:
		res = ADC0832.getResult() - 80
		if res < 0:
			res = 0
		if res > 100:
			res = 100
		print ('res = %d' % res)
		time.sleep(0.5)
		
		if res < 50:
			print("Light on")
			GPIO.output(LED, GPIO.HIGH)
		else:
			print("Light off")
			GPIO.output(LED, GPIO.LOW)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print ('The end !')
	finally:
		GPIO.cleanup()
