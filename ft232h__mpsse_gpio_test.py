# FT232H MPSSE GPIO tests using Python
#
# usage: sudo python ft232h__mpsse_gpio_test.py
#        or
#        clear; sudo python ft232h__mpsse_gpio_test.py
#
# @StephaneAG - 2015

# import the necessary libs
# std Python time lib
import time
# GPIO & FT232H modules
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

# tmp disable the built-in FTDI serial driver on Mac & Linux platforms
FT232H.use_FT232H()

# create an FT232H object that 'll grab the 1st FT232H device found & available
ft232h = FT232H.FT232H()


# == SETUP ==
# configure digital I/O using the setup function
# R: pin numbers 0 to 15 map to pins D0 to D7 then C0 to C7 on the board
ft232h.setup(7, GPIO.IN)   # Make pin D7 a digital input - connected to eiher Gnd or 5V
ft232h.setup(8, GPIO.OUT)  # Make pin C0 a digital output - connected to LED


# == LOOP ==
# loop turning the LED on and off and reading the input state
print 'Press Ctrl-C to quit.'
while True:
	# set pin C0 to a high level so the LED turns on.
	ft232h.output(8, GPIO.HIGH)
	# sleep for 1 second.
	time.sleep(1)
	# set pin C0 to a low level so the LED turns off.
	ft232h.output(8, GPIO.LOW)
	# sleep for 1 second.
	time.sleep(1)
	# read the input on pin D7 and print out if it's high or low.
	level = ft232h.input(7)
	if level == GPIO.LOW:
		print 'Pin D7 is LOW!'
	else:
		print 'Pin D7 is HIGH!'
