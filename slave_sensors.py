#!/usr/bin/python

import os

def get_temperature(sensor_id):
	try:
		with open("/sys/bus/w1/devices/28-" + sensor_id + "/w1_slave") as f:
			data = f.readlines()
		if data[0].strip()[-3:] != "YES":
			return 999
		else:	
			return float(data[1].split("=")[1])*0.001
	except:
		return 999

for sensor in os.listdir("/sys/bus/w1/devices"):
	if sensor.startswith("28-"):
		sensor_id=sensor[3:]
		print "ID:%s TEMP:%s" % (sensor_id,get_temperature(sensor_id))

