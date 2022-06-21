import RPi.GPIO as GPIO
import time
import subprocess
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def setAngle(angle):
    #2.5 to position to right side
    #12.5 to position to right side
    p.ChangeDutyCycle(angle)
    time.sleep(5)
    
try:
  setAngle(7.5) # initialize servo
  #print("1")
  f = open("/home/pi/a.txt","r")
  l = f.read(1)
  f.close()
  if (l=="1"):
    setAngle(4) # drop to left
  else:
    setAngle(11) # drop to right
    f2 = open("/home/pi/b.txt","w+")
    f2.write("1")
    f2.close()
  #subprocess.run(["python3","ul.py"])
#setAngle(2.5)
  setAngle(7.5) # reset servo to initial position
  p.stop()
  GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
