import RPi.GPIO as GPIO
import time

servopin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)


p = GPIO.PWM(servopin, 50)
p.start(2.5)

try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(12.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(2.5)
		time.sleep(0.5)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
