#!/usr/bin/python

import lcd
import time
import keys
from acmepins import GPIO 
import socket
from datetime import timedelta
import rs486
import os

led=GPIO("PB8","OUTPUT")
link=rs486.Link("/dev/ttyS2")

rx_counter=0
while True:
	message=link.receive(1)
	
	if message==None:
		print "timeout"
		continue
	
	try:
		led.on()
		rx_counter+=1
		print "%d] Rx %d %d" % (rx_counter,message.get_target_node(),message.get_frame_type())
		led.off()
	except:
		if rx_counter>0:
			rx_counter-=1
		continue									

