import ds18b20

for sensor in ds18b20.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor, ds18b20.get_temperature(sensor)))    