import microDBprocedures
import serial
import time


ser = serial.Serial('COM4')
line = ""
numberOfMicrobits = 0
print("connected to: " + ser.portstr)

def amountOfMicrobits():
    return numberOfMicrobits

while True:
  
    t = time.time()
    
    for symbol in ser.read():
        if t < (time.time() - 1.0): 
            #print(line + '\n') 
            x = line.split(",")
            if len(x) == 3:
                microbitID = int(x[0])
                if microbitID > numberOfMicrobits :
                    numberOfMicrobits = microbitID
                temperature = int(x[1])
                light = int(x[2])
                microDBprocedures.insertVariablesIntomicrobit(microbitID, temperature, light)
                microDBprocedures.insertVariablesIntomicrobitsummary(numberOfMicrobits, temperature, light)
            line = ""
        line = line + chr(symbol)          
    
    
    


