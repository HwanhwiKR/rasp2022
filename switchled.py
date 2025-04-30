import RPi.GPIO as GPIO 
from time import sleep 

RED= 8
GREEN = 16
switchR= 10
switchG = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switchR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(switchG, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(RED, GPIO.OUT) 
GPIO.setup(GREEN, GPIO.OUT) 

try: 
	while True:
		if GPIO.input(switchR)== GPIO.HIGH and GPIO.input(switchG)== GPIO.HIGH:
			print("BOTH ON")
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(GREEN, GPIO.HIGH)
			sleep(0.5)

		elif GPIO.input(switchR)== GPIO.HIGH:
			print("RED ON")
			GPIO.output(RED, GPIO.HIGH)
			sleep(0.5)

		elif GPIO.input(switchG)== GPIO.HIGH:
			print("GREEN ON")
			GPIO.output(GREEN, GPIO.HIGH)
			sleep(0.5)
		else:
			print("LED OFF")
			GPIO.output(RED, GPIO.LOW)
			GPIO.output(GREEN, GPIO.LOW)

finally:
	GPIO.cleanup() 
