import requests
import serial
import os, sys
import time
ser = serial.Serial('/dev/ttyACM0',9600, timeout = 5)
while True:
   line = ser.readline()
   hour = time.localtime(time.time()).tm_hour
   min = time.localtime(time.time()).tm_min
   sec = time.localtime(time.time()).tm_sec
   ard = {"time":"{}:{}:{}".format(hour, min, sec),"sensors":line}
   requests.post("https://jasmine.tzml-lab.tw/getInfo/", data = ard)
   if len(line) == 0:
      print("Time out! Exit.\n")
      sys.exit()
   print(ard)
