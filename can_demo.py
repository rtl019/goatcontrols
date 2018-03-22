import serial
import time

ser  = serial.Serial('/dev/ttyACM0', 9600)

print("CAN bus server interface demo")

while 1:
    ser.write(b'i')
    time.sleep(0.1)
    print(ser.readline())
    time.sleep(0.5)
    ser.write(b'm')
    time.sleep(0.1)
    print(ser.readline())
    time.sleep(0.5)
    ser.write(b'k')
    time.sleep(0.1)
    print(ser.readline())
    time.sleep(0.5)
    ser.write(b'c')
    time.sleep(0.1)
    print(ser.readline())
    time.sleep(0.1)
