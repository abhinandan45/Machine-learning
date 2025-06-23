from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route("/prediction_form")
def prediction_form():
    return render_template("formm.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        areaa = request.form['area']
        bed = request.form['bedrooms']

        input = pd.DataFrame([[float(areaa), float(bed)]], columns=['area', 'bedrooms'])
        output = model.predict(input)

        return render_template("formm.html", pred=output[0])
    else:
        return "not run"

if __name__ == "__main__":
    app.run(debug=True)
