import requests
import serial
import os, sys
import time
ser = serial.Serial('/dev/ttyACM0',9600, timeout = 10)
ser.flush()
token = ""
with open("./recvToken/token", "r") as f:
    token=f.readline()
count = 0
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
        if count == 10:
            requests.post("https://kaibao.tzml-lab.tw/rspcontroller/sensorData?token="+token, data = ard)
            count = 0
    except:
        continue
    count = count+1
    print(ard)
    #time.sleep(10)
