import time
import serial
ser = serial.Serial()
ser.port = 'com4'
ser.open()
print("We are done setting") 

while(1):
    ser.write(b'L')
    print("Wrote 1")
    time.sleep(1)
    ser.write(b'q')
    print("Wrote q")
    time.sleep(1)


