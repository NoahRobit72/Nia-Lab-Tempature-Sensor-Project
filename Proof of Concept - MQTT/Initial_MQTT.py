import paho.mqtt.client as mqtt
#import matplotlib.pyplot as plt
import numpy as np
import time


mqtt_broker = "192.168.1.125"

# Create Clients
client1 = "temp1"
client2 = "temp2"


f1 = open("dataFile1.txt", "wb")
f2 = open("dataFile2.txt", "wb")

## make empty numeric arrays
temp1Data = []
temp2Data = []

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    client.subscribe(client1)
    client.subscribe(client2)

def print_message(sender, msg):
    if(sender == client1):
        f1.write(msg + "\n")
    elif(sender == client2):
        f2.write(msg + "\n")

# This function writes to a .txt file. It writes a string
def add_to_array(sender, msg):
    if(sender == client1):
        
        temp1Data.append(float(msg))
    elif(sender == client2):
        temp2Data.append(float(msg))


def on_message(client, userdata, msg):
    print("The tempature from " + msg.topic + " is: " + msg.payload)
    print_message(msg.topic, msg.payload)
    add_to_array(msg.topic, msg.payload)



            
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker, 1883, 60)

client.loop_forever()
fo.close()
