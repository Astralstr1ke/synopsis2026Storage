import RPi.GPIO as GPIO
import time
import asyncio
import socket
async def sendPackage(package):
    message='$' + package + '$' +  unitNR + '$' + '1'
    HOST, PORT = "Controller Module", 5560
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(message)
    sock.close


GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
unitNR = 1


print ("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time() 
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  if distance >= 10 & distance <= 30:
            try:
                asyncio.run(sendPackage(pulse_end))
            except:
                break


GPIO.cleanup()

