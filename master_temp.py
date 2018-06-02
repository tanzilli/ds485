import rs485	
import time

# Apre la linea seriale sulla RS485
link=rs485.Link("/dev/ttyS2")

# Invia la richiesta di lettura ad un nodo
message=rs485.Payload(2)

while True:
	# Invia la richiesta di lettura ad un nodo
	message=rs485.Payload(2)
	link.send(message)

	# Aspetta la risposta
	incoming_message=link.receive()

	# Controlla se e' arrivata la risposa
	if incoming_message==None:
		print "Timeout"
		time.sleep(1)
		continue
	else:
		sensors=incoming_message.get()
		for sensor in sensors:
			print "Id=%s Temp=%.1f" % (sensor,sensors[sensor])
		print " "	
		time.sleep(1)




