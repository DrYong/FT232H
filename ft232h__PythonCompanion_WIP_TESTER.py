#!/usr/bin/python
import time
import serial
import sys
import json

def ftdi232h_cmd(thePort, theBaud, theCommand):
 ser = serial.Serial(
  port=thePort, # /dev/ttyUSB0
  baudrate=theBaud, # 9600
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  xonxoff=0, rtscts=0, dsrdtr=0,
 )
 ser.isOpen()
 ser.write(theCommand+"\n")
 endtime = time.time()+1 #0.2 # wait 0.2 sec
 result = ""
 while time.time() < endtime:
   while ser.inWaiting() > 0:
     #result=result+ser.read(1)
     result=result+ser.read()
     #result=ser.read()
 ser.close()
 #return result
 return 'callback: ['+result.rstrip('\n')+']'

if len(sys.argv)!=4:
 print "USAGE: ft232h__PythonCompanion_WIP_TESTER.py "+'"'+"<port> <baud> <serial message>"+'"'
 exit(1)

print ftdi232h_cmd(sys.argv[1], sys.argv[2], sys.argv[3]).strip()



'''

import time
import serial
import sys
import json
ser = serial.Serial(
port='/dev/ttyUSB0', # or /dev/ttyAMA0 for serial on the Raspberry Pi
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
xonxoff=0, rtscts=0, dsrdtr=0,
)
ser.isOpen()
result = ""
ser.write("1"+"\n")
while ser.inWaiting() > 0:
  result=result+ser.read()
  
result

'''
