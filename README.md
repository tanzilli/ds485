# DS485 firmware

La DS485 è una scheda Linux basata sul modulo [Arietta G25](https://www.acmesystems.it/arietta) progettato per fare 
da collettore dati tra un gruppo di sensori 1-wire DS18B20 ed un bus RS485.

Il firmware è stato sviluppato interamente in Python e consente di:

* Gestire il rivelamento automatico dei sensori DS18B20 connessi ai 4 bus 1-wire di cui è dotata la scheda
* Visualizzare su un display LCD alfanumerico 16x2 retroilluminato le letture di temperature 
* Gestire una semplice interfaccia utente per l'installatore per verificare la corretta funzionalità dei sensori connessi e impostare l'indirizzo sul bus RS485 del concentratore
* Inviare in remoto i dati istantanei di temperatura letti
* Consentire di pilotare il relè a bordo con comandi RS485

Il modulo firmware principale che gira su ogni Arietta si chiama [ds485.py](ds485.py)

Da una Raspberry Pi + possibile interrogare più moduli Arietta G25 tramite una sola interfaccia RS485

Ecco alcuni programmi d'esempio per la Raspberry Pi che fa da concentratore:

* [try_read.py](try_read.py) che legge e visualizza i dati provenienti dai concentratori DS485 sul campo
* [try_relay.py](try_relay.py) che accende e spegne un relè su un dato concentratore

## Installazione su Arietta G25

  git clone https://github.com/tanzilli/ds485.git

## Links 

* <http://www.tanzolab.it/DS485>
