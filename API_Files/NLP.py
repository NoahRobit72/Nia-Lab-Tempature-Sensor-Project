from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

class NLP(Resource):
    # def get(self):
    #     parser = reqparse.RequestParser()  # initialize
        
    #     # adding name and ID to NLP analysis 
    #     parser.add_argument('userId', required=True)  # add args
    #     parser.add_argument('name', required=True)
        
    #     return {"data": "Natural Language is processed!"}
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        # adding name and ID to NLP analysis 
        parser.add_argument('name', required=True)  # add args
        parser.add_argument('password', required=True)
                
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        for key in args:
            print(key, '->', args[key])
        
        print("below is the indexed args: ")    
        
        values = args.values()
        values_list = list(values)
        a_value = values_list[1]
        
        lines = [values_list[1]]
        with open('INFO.txt', 'w') as f:
            f.writelines(lines)

        print(a_value)  
   
        
        return {"data": "Natural Language is processed!"}
    
    
    
    