# microbit radio sender temperature and light by Mattias Olofsson
from microbit import *
import radio

# Event loop.
while True:
    #put of radio
    radio.off()
    # wait 10 seconds before sending again.
    sleep(10000)
    # put on radio
    radio.on()
    # Temperature meassure
    temp = str(temperature())
    # Light meassure
    lightLevel = str(display.read_light_level())
    #  message of temperature and light
    message = temp + ',' + lightLevel
    #Send temperature and light 
    radio.send(message)  # a-ha

    
