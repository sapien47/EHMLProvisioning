from flask import Flask, Response, request
from functools import wraps
from Model.ModelBuilder import LinearRegressionModel
import numpy as np

model = LinearRegressionModel()

app = Flask(__name__)
port = 9001

@app.route('/', methods=['GET', 'POST'])
def service():
    return "Welcome to our prediction Service"

@app.route('/predict', methods=['GET'])
def prediction(bi):
    if request.method == 'GET':
        x = float(request.args.get('x'))
        input = np.array([x]).reshape(-1,1)

        res = model.makePrediction(x_data=input)
        return np.array_str(res)
    return ""

if __name__ == '__main__':
    model.trainModel()
    app.run(host='0.0.0.0', port=port, threaded=True)
