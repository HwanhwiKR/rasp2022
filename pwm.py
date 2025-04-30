import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 10
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)

while True:
	GPIO.output(led, GPIO.HIGH)
	time.sleep(0.05)

	GPIO.output(led, GPIO.LOW)
	time.sleep(0.01)
