#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://mysqlclient.readthedocs.io/user_guide.html
# MySQLDB: letture
# User: pi
# Password: acmesystems

import _mysql
import rs485	
import time



node_addrs=[1,2]


db=_mysql.connect(host="localhost",user="pi",passwd="acmesystems",db="letture")

if True:
	db.query("DROP TABLE IF EXISTS Temperatures")
	db.query("CREATE TABLE Temperatures(Id INT PRIMARY KEY AUTO_INCREMENT, \
				Date DATETIME, \
				SensorId VARCHAR(25), \
				Temperature FLOAT \
				)")
		 
# Apre la linea seriale sulla RS485
link=rs485.Link("/dev/ttyUSB0")

while True:
	node_counter=0
	for node_addr in node_addrs:	
		print "TX] Nodo %d" % node_addr
		link.send(rs485.Packet(node_addr))

		# Aspetta la risposta
		reply=link.receive()

		# Controlla se e' arrivata la risposa
		if reply==None:
			print "RX] Node %d Timeout " % (node_addr)
		else:
			try:
				sensors=reply.get()
				for sensor in sensors:
					sql_query="INSERT INTO Temperatures(Date,SensorId,Temperature) VALUES(now(),'%s',%.2f)" % (sensor,sensors[sensor])
					#print sql_query
					db.query(sql_query)
		
			except Exception as e: 
				print(e)
				print "RX] Error"
				continue

		node_counter+=1
		if node_counter==2:
			node_counter=0
	
		time.sleep(0.02)
	time.sleep(60)	