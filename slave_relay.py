#!/usr/bin/python

from acmepins import GPIO 
from time import sleep

relay=GPIO("J4.29","OUTPUT")

while True:
	relay.on();
	sleep(1);
	relay.off();
	sleep(1);
