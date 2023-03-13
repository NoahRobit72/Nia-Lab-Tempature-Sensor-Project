from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

class TEMP2(Resource):
    
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
        
        return {"data": "Tempature 1 has been received"}
    
    
    
    