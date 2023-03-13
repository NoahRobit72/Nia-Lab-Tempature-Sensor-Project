## This project is a template to how the Nia Lab Tempature Sensor Project will parse and store tempature date

### SQL Structure
The project will contain one database with mutiple tables.  
Each table will be for each tempature sensor. As an example, if there are five tempature sensors, there will be 5 tables.  
  
Each table will be structured as the following:  
| Date | Time | Tempature Reading |  
  
Addationally the tables will follow the convention of temp_table_1...temp_table_2...  
Each table will correspond with a tempature sensor located in one location in the lab

### HTTP Structure
The main component of the project is an API that will be built to collect the data from the tempature sensors.  
The API can be called from any of the tempature sensors. Below is the structure of the HTTP request that will be sent from ther sensors.   
  
