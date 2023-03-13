## Nia Lab Tempature Sensor Project 

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
   
__Tempature Sensor:__ Which tempature sensor in the lab the request is coming from  
__Date:__ mm dd yr. 
__Time:__ Time of day in 24 hour clock  
__Tempature:__ Tempature in celsius. 
  
