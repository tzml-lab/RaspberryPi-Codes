import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setwarnings(False)
s = socket.socket()
host = "0.0.0.0"
port = 123
s.bind((host, port))
 
s.listen(5)
while True:
    c,addr = s.accept()
    print(addr)
    req = c.recv(1024)
    print("Recv:", req)
    if int(req) == 1:
        GPIO.output(7,GPIO.HIGH)
        print("ON")
    elif int(req) == 2:
        GPIO.output(7,GPIO.LOW)
        print("OFF")
    else:
        break
    c.send(b'success')	
c.close()
s.close()

GPIO.cleanup()

