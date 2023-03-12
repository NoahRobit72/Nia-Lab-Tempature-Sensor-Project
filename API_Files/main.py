from flask import Flask
from flask_restful import Api, Resource

# Import the classes from the files
from NLP import NLP
from SFU import SFU
from NFI import NFI


app = Flask(__name__)
api = Api(app)
    
# Adding the paths and classes
api.add_resource(NLP, "/NLP")
api.add_resource(NFI, "/NFI")
api.add_resource(SFU, "/SFU")


if __name__ == "__main__":
    app.run(debug=True)