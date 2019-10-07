import microDBprocedures
import serial
import time


ser = serial.Serial('COM4')
line = ""
print("connected to: " + ser.portstr)

while True:
  
    t = time.time()
    
    for symbol in ser.read():
        if t < (time.time() - 1.0): 
            #print(line + '\n') 
            x = line.split(",")
            if len(x) == 2:
                temperature = int(x[0])
                light = int(x[1])
                microDBprocedures.insertVariablesIntomicrobit(temperature, light)
                microDBprocedures.insertVariablesIntomicrobitsummary(temperature, light)
            line = ""
        line = line + chr(symbol)          
    
    
    


