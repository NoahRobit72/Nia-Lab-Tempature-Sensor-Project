from flask import Flask
from flask_restful import Api, Resource

class TEMP1(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        # adding name and ID to NLP analysis 
        parser.add_argument('Date', required=True)  # add args
        parser.add_argument('Time', required=True)
        parser.add_argument('Tempature', required=True)
                
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        for key in args:
            print(key, '->', args[key])
        
   
        return {"data": "Tempature 2 has been received"}
    