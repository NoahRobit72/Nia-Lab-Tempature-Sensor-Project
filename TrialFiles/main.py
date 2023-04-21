from flask import Flask
from flask_restful import Api, Resource

# Import the classes from the files
from TEMP1 import TEMP1
from TEMP2 import TEMP2


app = Flask(__name__)
api = Api(app)
    
# Adding the paths and classes
api.add_resource(NLP, "/TEMP1")
api.add_resource(NFI, "/TEMP2")


if __name__ == "__main__":
    app.run(debug=True)