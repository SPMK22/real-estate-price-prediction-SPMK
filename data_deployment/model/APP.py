from flask import Flask, request
from flask import Flask, render_template

import pickle

app = Flask(__name__)

# Load the pickled model from disk
with open("model.pickle", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the request body
    input_data = request.get_json()
    
    # Use the model to make a prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return {"prediction": prediction}

if __name__ == "__main__":
    app.run()
