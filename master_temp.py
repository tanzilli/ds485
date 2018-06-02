import rs485	
import time

# Apre la linea seriale sulla RS485
link=rs485.Link("/dev/ttyS2")

while True:
	# Invia la richiesta di lettura al nodo n.2
	link.send(rs485.Packet(2))

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
			print "Id=%s Temp=%.1f" % (sensor,sensors[sensor])
		print " "	
		time.sleep(1)




