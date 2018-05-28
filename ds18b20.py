import os

BASE_DIRECTORY = "/sys/bus/w1/devices"
SLAVE_PREFIX = "28-"
SLAVE_FILE = "w1_slave"

def get_available_sensors():
	sensors = []
	for sensor in os.listdir(BASE_DIRECTORY):
		if sensor.startswith(SLAVE_PREFIX):
			sensors.append(sensor[3:])
	return sensors

def get_sensor_value(sensor):
	with open(BASE_DIRECTORY+"/"+SLAVE_PREFIX+sensor+"/"+SLAVE_FILE) as f:
		data = f.readlines()

	if data[0].strip()[-3:] != "YES":
		raise SensorNotReadyError()
	return float(data[1].split("=")[1])*0.001


#https://github.com/rgbkrk/ds18b20