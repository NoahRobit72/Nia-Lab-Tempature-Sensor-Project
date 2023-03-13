import time
import board
import busio
import adafruit_sht31d
import adafruit_requests as requests
import neopixel
from umqtt.robust import MQTTClient

# Configure WiFi and MQTT credentials
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
MQTT_BROKER = "YOUR_MQTT_BROKER_IP_ADDRESS"
MQTT_CLIENT_ID = "YOUR_MQTT_CLIENT_ID"
MQTT_TOPIC = "YOUR_MQTT_TOPIC"

# Initialize I2C and sensors
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

# Initialize neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)

# Connect to WiFi
print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    pass
print("Connected to WiFi:", wifi.ifconfig())

# Connect to MQTT broker
print("Connecting to MQTT broker...")
mqtt = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
mqtt.connect()
print("Connected to MQTT broker")

# Main loop
while True:
    # Read sensor data
    temperature = sensor.temperature
    humidity = sensor.relative_humidity

    # Send sensor data to MQTT broker
    mqtt.publish(MQTT_TOPIC, '{"temperature":' + str(temperature) + ',"humidity":' + str(humidity) + '}')

    # Blink neopixel to indicate data transmission
    pixels[0] = (0, 255, 0)
    time.sleep(0.5)
    pixels[0] = (0, 0, 0)

    # Wait for some time before sending next data
    time.sleep(10)
