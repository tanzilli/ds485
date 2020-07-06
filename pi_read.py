import rs485	
import time

node_addrs=[1,2]
good_packet=[0,0]
bad_packet=[0,0]

# Apre la linea seriale sulla RS485
link=rs485.Link("/dev/ttyUSB0")

while True:
	node_counter=0
	for node_addr in node_addrs:	
		#print "TX] Nodo %d" % node_addr
		link.send(rs485.Packet(node_addr))

		# Aspetta la risposta
		reply=link.receive()

		# Controlla se e' arrivata la risposa
		if reply==None:
			print "RX] Node %d Timeout " % (node_addr)
			bad_packet[node_counter]+=1
		else:
			try:
				sensors=reply.get()
				for sensor in sensors:
					print "RX] Node=%d Id=%s Temp=%.2f" % (node_addr,sensor,sensors[sensor])
					pass
				print " "	
				good_packet[node_counter]+=1
			except:
				print "RX] Error"
				continue

		node_counter+=1
		if node_counter==2:
			node_counter=0
			
		time.sleep(0.05)
	



