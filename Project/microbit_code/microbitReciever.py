# microbit radio recieve temperature and light
# and sends it by serial to a program listening on the usbport
# by Mattias Olofsson
from microbit import *
import radio

radio.on()
uart.init()

while True:
    
    incoming = radio.receive()
    if incoming:
        uart.write(incoming)