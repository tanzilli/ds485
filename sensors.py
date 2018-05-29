import ds18b20

sensors = []
for sensor_id in ds18b20.get_available_sensors():
    sensors.append(sensor_id)

for sensor in sensors:
    print("Sensor %s has temperature %.2f" % (sensor, ds18b20.get_temperature(sensor)))