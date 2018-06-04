# DS485 firmware

La DS485 è una scheda Linux basata sul modulo [Arietta G25](https://www.acmesystems.it/arietta) progettato per fare da collettore dati tra un gruppo di sensori 1-wire DS18B20 ed un bus RS485.

Il firmware è stato sviluppato interamente in Python e consente di:

* Gestire il rivelamento automatico dei sensori DS18B20 connessi ai 4 bus 1-wire di cui è dotata la scheda
* Visualizzare su un display LCD alfanumerico 16x2 retroilluminato le letture di temperature 
* Gestire una semplice interfaccia utente per l'installatore per verificare la corretta funzionalità dei sensori connessi e impostare l'indirizzo sul bus RS485 del concentratore
* Inviare in remoto i dati istantanei di temperatura letti
* Consentire di pilotare il relè a bordo con comandi RS485

Il modulo firmware principale si chiama [main.py](main.py)

Esistono due programmi di esempio sempre in Python per poter sviluppare il master RS485 in grado di interrogare i nodi che
sono:

* [read_temp.py](read_temp.py) che legge e visualizza i dati provenienti dai concentratori DS485 sul campo
* [relay.py](relay.py) che accende e spegne un relè su un dato concentratore

* main.py
  Programma da lanciare sulla scheda DS485
* master_temp.py
  Programma di prova per leggere le temperature dalle schede remote via RS485

## Installazione

  git clone https://github.com/tanzilli/ds485.git

## Links 

* <http://www.tanzolab.it/DS485>
