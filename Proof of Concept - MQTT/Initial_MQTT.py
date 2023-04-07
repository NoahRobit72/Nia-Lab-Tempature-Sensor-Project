import paho.mqtt.client as mqtt

mqtt_broker = "your_MQTT_BROKER_IP_ADDRESS"

# add an empty string vector

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    #init_plot       inilize plot
    client.subscribe("esp32/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #array.append(strToInt(msg.payload)        call function to turn string into data value. 
    #storeInFile(strToInt(msg.payload))
    #updatePlot(array name)
    
    
# def function to turn the msg into a int value
    # return a int

    
# def print value (value array)
    # stuff to print plot
  
#initilize the file I/O and the plot
#def init_Actions
    #inlilie plot with features 
 
# def storeInFile(msg)
    #fo = open("dataFile1.txt", "wb")
    #fo.write( "msg+"\n")




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker, 1883, 60)

client.loop_forever()
