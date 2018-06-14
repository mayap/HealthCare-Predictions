from flask import Flask
from flask import request, render_template
from flask_cors import CORS
import json

# Importing classifier from classifier folder
from classifier.decisionTreeClassifier import main
from classifier.decisionTreeClassifier import predict


app = Flask(__name__)
CORS(app)
data = main()


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/tree')
def tree():
    return render_template('tree.html')


@app.route('/prediction', methods=['POST'])
def makePrediction():
    # Get data from POST request
    content = request.get_json()
    predict_data = []

    # Convert received data to float number
    for number in content:
        predict_data.append(float(number))

    # Predict class for the received data
    results = predict(predict_data, data)

    # Return json
    return json.dumps(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
