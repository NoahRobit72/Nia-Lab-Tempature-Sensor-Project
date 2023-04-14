#include <WiFi.h>
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const char* ssid = "Test";
const char* password = "smartsys";
const char* mqtt_server = "192.168.1.125";

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;     
// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);


WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);
  //Serial.println("ºC");
  char buffer[10];
  dtostrf(temperatureC, 4, 2, buffer);
<<<<<<<< HEAD:Proof of Concept - MQTT/Initial_MQTT/Initial_MQTT.ino
  client.publish("temp1", buffer);
========
  client.publish("esp32/temp1", buffer);
>>>>>>>> c9c4e19a8830c9b450f5e70ec4f274ffe91e31c8:Proof of Concept - MQTT/Initial_MQTT_test1.ino

  delay(5000);
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT Broker...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT Broker");
    } else {
      Serial.print("Failed with error code: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}
