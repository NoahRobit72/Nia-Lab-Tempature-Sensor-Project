import paho.mqtt.client as mqtt

# Configure MQTT credentials
MQTT_BROKER = "YOUR_MQTT_BROKER_IP_ADDRESS"
MQTT_TOPIC = "YOUR_MQTT_TOPIC"

# Define callback functions for MQTT client
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("Received message on topic "+msg.topic+" with payload "+str(msg.payload))

# Connect to MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)

# Main loop to keep receiving MQTT messages
client.loop_forever()
