from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("house_model.pkl")

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/eda")
def eda():
    return render_template("eda.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None
    if request.method == "POST":
        area = float(request.form["area"])
        bathrooms = int(request.form["bathrooms"])
        stories = int(request.form["stories"])
        parking = int(request.form["parking"])
        airconditioning = int(request.form["airconditioning"])
        semi_furnished = int(request.form["semi_furnished"])
        unfurnished = int(request.form["unfurnished"])

        data = pd.DataFrame([[area, bathrooms, stories, parking,
                              airconditioning, semi_furnished, unfurnished]],
                            columns=['area', 'bathrooms', 'stories', 'parking',
                                     'airconditioning',
                                     'furnishingstatus_semi-furnished',
                                     'furnishingstatus_unfurnished'])

        result = model.predict(data)[0]

    return render_template("predict.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
