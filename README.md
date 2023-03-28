## Nia Lab Tempature Sensor Project 
## Hardware
The hardware for the project will consit of a number of Adafruit HUZZAH32 - ESP32 Feather boards that will host the tempature sensors.  

## Software: Option 1
This first option consists of using MQTT communication to send data from the devices to the Rasberry Pi server. On the server, there will be a firebase NoSQL database that will host the tempature data. On the server, there will be a python script to request and analyze the python data.  

## Software: Option 2
This option uses BLE Communication to send data from the client (esp32) to the server (Pi)

## Software: Option 3
This second option consists of using HTTPS request (URI) to send data from the ESP32 devices to the Rasberry Pi module. Once recieved on the Rasberry Pi module, a python script will parse the URI and post the data into a MySQL database.   

### SQL Structure
The project will contain one database with mutiple tables.  
Each table will be for each tempature sensor. As an example, if there are five tempature sensors, there will be 5 tables.  
  
Each table will be structured as the following:  
| Date | Time | Tempature Reading |  
  
Addationally the tables will follow the convention of temp_table_1...temp_table_2...  
Each table will correspond with a tempature sensor located in one location in the lab

### HTTP Structure
The main component of the project is an API that will be built to collect the data from the tempature sensors.  
The API can be called from any of the tempature sensors. Below is the structure of the HTTP request that will be sent from ther sensors:  
  
http //127.0.0.1:5000/__Tempature_Sensor__?__Date__=10102023&__Time__=2139&__Tempature__=76  
   
__Tempature Sensor (string):__ Which tempature sensor in the lab the request is coming from  
__Date (int):__ mm dd yr   
__Time (int):__ Time of day in 24 hour clock  
__Tempature (int):__ Tempature in celsius. 
  
