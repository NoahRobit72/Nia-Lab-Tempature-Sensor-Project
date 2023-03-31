## Nia Lab Tempature Sensor Project 
## Hardware
The hardware for the project will consit of a number of Adafruit HUZZAH32 - ESP32 Feather boards that will host the tempature sensors.  

## Data Protocol
### Option 1: MQTT
This first option consists of using MQTT communication to send data from the devices to the Rasberry Pi server. On the server, there will be a firebase NoSQL database that will host the tempature data. On the server, there will be a python script to request and analyze the python data.  

### Option 2: Bluetooth Low Energy (BLE)
This option uses BLE Communication to send data from the client (esp32) to the server (Pi)

### Option 3: Hypertext Transfer Protocol (HTTP)
This second option consists of using HTTPS request (URI) to send data from the ESP32 devices to the Rasberry Pi module. Once recieved on the Rasberry Pi module, a python script will parse the URI and post the data into a MySQL database. 


## Data Storage
### Option 1: File I/O
This project will input the data into a .txt file that can be read at a later time.

### Option 2: MySQL
The project will contain one database with mutiple tables.  
Each table will be for each tempature sensor. As an example, if there are five tempature sensors, there will be 5 tables.  
  
Each table will be structured as the following:  
| Date | Time | Tempature Reading |  
  
Addationally the tables will follow the convention of temp_table_1...temp_table_2...  
Each table will correspond with a tempature sensor located in one location in the lab

  
