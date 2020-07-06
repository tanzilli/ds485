#!/usr/bin/python

from time import sleep
import keys

key=keys.KEYS()


while True:
	if key.hit():
		print key.get()