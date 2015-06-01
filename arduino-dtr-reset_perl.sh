#!/usr/bin/perl

# R: sudo apt-get install libdevice-serialport-perl

perl -MDevice::SerialPort -e 'Device::SerialPort->new("/dev/rfcomm0")->pulse_dtr_on(1000)';
