import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
count=0
slot=10
while True:
  print "Ultrasonic Measurement"

  # Set pins as output and input
  GPIO.setup(16,GPIO.OUT)  # Trigger
  GPIO.setup(18,GPIO.IN)      # Echo
  
  # Set trigger to False (Low)
  GPIO.output(16, False)
  

  # Allow module to settle
  time.sleep(0.5)

  # Send 10us pulse to trigger
  GPIO.output(16, True)
  time.sleep(0.00001)
  GPIO.output(16, False)
  start = time.time()
  while GPIO.input(18)==0:
    start = time.time()

  while GPIO.input(18)==1:
    stop = time.time()

  # Calculate pulse length
  elapsed = stop-start

  # Distance pulse travelled in that time is time
  # multiplied by the speed of sound (cm/s)
  distance = elapsed * 34000

  # That was the distance there and back so halve the value
  distance = distance / 2

  print "Distance : %.1f" % distance, "cm"
  time.sleep(2)
  
  if(distance<=60 and distance>=20):
    count=count+1
    slot=slot-1
    
    if(count>=10 and slot<=1):
      print"the slots are full"
      break;
    print"No of Vechiless enterd",count
    print"No of slots free",slot
    time.sleep(2)
  
    # Set pins as output and input
  GPIO.setup(3,GPIO.OUT)  # Trigger
  GPIO.setup(5,GPIO.IN)      # Echo
  
  # Set trigger to False (Low)
  GPIO.output(3, False)
  
  # Allow module to settle
  time.sleep(0.5)

  # Send 10us pulse to trigger
  GPIO.output(3, True)
  time.sleep(0.00001)
  GPIO.output(3, False)
  start1 = time.time()
  while GPIO.input(5)==0:
    start1 = time.time()

  while GPIO.input(5)==1:
    stop1 = time.time()

  # Calculate pulse length
  elapsed1 = stop1-start1

  # Distance pulse travelled in that time is time
  # multiplied by the speed of sound (cm/s)
  distance1 = elapsed1 * 34000

  # That was the distance there and back so halve the value
  distance1 = distance1 / 2

  print "Distance : %.1f" % distance1, "cm"
  
  if(distance1<=60 and distance1>=20):
    slot=slot+1
    count=count-1
    if(count<=1 and  slot>=10):
        print"slots are empty"
        break;
    print"No of Vechiless left",count
    print"No of slots Available",slot
    time.sleep(2)

# Reset GPIO settings
GPIO.cleanup()
