import pandas as pd
import numpy as np
from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
import argparse
import json

app = Flask(__name__)
api = Api(app)

class OBM(Resource):
    #http get delete put post methods go here
    def get(self):
        with open('OBM.json') as f:  # read local CSV
            data = json.load(f) # convert dataframe to dict
        return  data, 200  # return data and 200 OK
    

    

api.add_resource(OBM, '/obm')

if __name__ == '__main__':
    app.run()



#print(pd.read_csv("angry_moods.csv"))


