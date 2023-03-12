## Here I an APIs with three different endpoints (destinations):
* Secure File Uploader/Ingester
* Text NLP Analysis
* News feed Ingester

## March 12th - Present
### Building out MySQL
Currently I am using one database called "geeks" (It will be changed soon).
In the database there is currently one table that will host all of the user information. 
Right now we have two columns. One is username and the other is password. 

### Parsing the users information
As API gets information form the HTTP request, the python script will parse the information and input it into the sql database.  
The next step in this process is to built a function that can be called with input arguments of table, username, and password.  


## March 10th - March 12th
### Transition to MySql Server
Building the project with MySql Server  
Project database outline found (found [here](https://www.freecodecamp.org/news/connect-python-with-sql/))
  
We are going to locally host the MySQL database with (found [here](https://www.geeksforgeeks.org/how-to-connect-python-with-sql-database/))

## Begining - March 10th
### Why Mongo DB?
1.  The document-oriented approach allows non-defined attributes to be modified on the fly. This is a key contrast between MongoDB and other relational databases. 
2.  JSON is widely used across for frontend and API communication. It only makes sense for the database to use the same protocol. 


### Database Structure

There will be three containers for Users, File Storage, and Text Analysis.  
Additionally, there will be documents for each of the users in our system. 

* User:
	* User ID: 
	* Username:
	* Password:

* Files Storage:
 	* User ID:
	* File ID:
	* File Name:
	* File Type:
	* Favorite Status:
	* Date of creation:


* Text Analysis:
	* File ID:
	* Sentiment Analysis:
	* Summary Analysis:


### Database Implementation
While this project is one API, the API will have three different endpoints that will correspond to each of the three functions. 
Because of the mutiple endpoints, we will have to input the "user" and "userID" for every API call.  
  
I am still working out what information I would like to "store" in a data structure in the class and what data to send to the database.   
Addationally, I am still working through what steps I need to take to filter data before I input it into the data base.

### Setps For Setting up MongoDB
1. Begin with writing code to be able to parse user information (found [here](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f))
2. Implement simple mongoDB that will store the "user" and "userID" information


