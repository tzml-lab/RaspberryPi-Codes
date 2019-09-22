import requests
import serial
import os, sys
import time
ser = serial.Serial('/dev/ttyACM2',9600, timeout = 5)
ser.flush()

while True:

    try:
        #line = ser.readline()
        line = "data,28.0,30.0,0000,0111.66,\r\n"
        line = ser.read(len(line))
        print("read...")
        print(line)
        if len(line) != 30:
            print("Loss")
            ser.flush()
            ser.flushInput()
            continue
        #line += ser.read(ser.inWaiting())
    except:
        continue
    
    if len(line) == 0:
        print("time out")
        continue
    str = line.decode("utf-8")
    print(str)
    sensorVal = str.split(',',6)
    print(sensorVal)
    if(len(sensorVal)) != 6:
        print("format wrong")
        continue
    for i in range(len(sensorVal)):
        if sensorVal[i] == ' ':
            sensorVal = 'Err'
            
    
    hour = time.localtime(time.time()).tm_hour
    min = time.localtime(time.time()).tm_min
    sec = time.localtime(time.time()).tm_sec
    ard = {"time":"{}:{}:{}".format(hour, min, sec),"height":0,"temp":sensorVal[1],"humidity":sensorVal[2],"soil_humidity":sensorVal[3],"light":sensorVal[4]}
    try:
        requests.post("https://jasmine.tzml-lab.tw/getInfo/a/", data = ard)
    except:
        continue
    
    print(ard)
