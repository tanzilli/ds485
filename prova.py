

class KEYS():
	totale=0
	
	def conta(self,finoa):
		self.totale=self.totale+finoa
		for i in range(finoa):
			print i+1

	def dimmitotale(self):
		return self.totale


contatore1=KEYS()
contatore2=KEYS()

contatore1.conta(10)
contatore2.conta(2)
contatore1.conta(2)
contatore2.conta(10)

print "totale1=", contatore1.dimmitotale()
print "totale2=", contatore2.dimmitotale()



