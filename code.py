import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
while True:
    if(GPIO.input(11)==1):
        GPIO.output(13,True)
        print"Person Detected"
	time.sleep(1)
        else:
        GPIO.output(13,False)
        print"Person not detected"
	time.sleep(1)
         GPIO.cleanup()
