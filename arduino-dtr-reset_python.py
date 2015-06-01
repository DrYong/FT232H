#!/usr/bin/python

import sys, serial, time
ser = serial.Serial('/dev/rfcomm0', 57600)
ser.setDTR(0)
time.sleep(0.1)
ser.setDTR(1)
ser.close()
