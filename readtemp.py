import rs485	
import time

node_addrs=[2,3]

# Apre la linea seriale sulla RS485
link=rs485.Link("/dev/ttyUSB0")

while True:
	for node_addr in node_addrs:	
		# Invia la richiesta di lettura al nodo n.2
		link.send(rs485.Packet(node_addr))

		# Aspetta la risposta
		reply=link.receive()

		# Controlla se e' arrivata la risposa
		if reply==None:
			print "Timeout"
			time.sleep(1)
			continue
		else:
			sensors=reply.get()
			for sensor in sensors:
				print "Node=%d Id=%s Temp=%.2f" % (node_addr,sensor,sensors[sensor])
			print " "	
			time.sleep(1)




