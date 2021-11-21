import serial
import time
#from serial.serialutil import to_bytes
ser = serial.Serial("COM5")

while(True):
    N=bytes("N",'utf-8')
    F=bytes("F",'utf-8')
    #print(type(x))
    ser.write(N)
    time.sleep(1)
    ser.write(F)
    time.sleep(1)
    
