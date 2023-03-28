import serial
ser = serial.Serial('/dev/rfcomm0', baudrate=9600)
while True:

Bluetooth for Raspberry PI 3

message = ser.readline()
print(message.decode().strip())
