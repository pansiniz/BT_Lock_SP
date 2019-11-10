import RPi.GPIO as GPIO
import time
R=21
G=20
B=16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(R,GPIO.OUT)
GPIO.output(R,0)
GPIO.setup(G,GPIO.OUT)
GPIO.output(G,0)
GPIO.setup(B,GPIO.OUT)
GPIO.output(B,0)

i=1
while i>0:

	if (i==1):
		GPIO.output(R,1)
		GPIO.output(G,0)
		GPIO.output(B,0)
		i=2
		time.sleep(.1)
	elif (i==2):
		GPIO.output(R,0)
		GPIO.output(G,0)
		GPIO.output(B,1)
		i=1
		time.sleep(.1)
