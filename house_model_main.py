from flask import Flask, render_template, request
import pandas as pd
import joblib
import pymysql
import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="flask",
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)

model = joblib.load("house_model.pkl")
furnishing_encoder = joblib.load("furnishing_encoder.pkl") 

@app.route("/submitdata")
def submitdata():
    query1 = "insert into students(id,name,city)values(%s,%s,%s)"
    cursor = con.cursor()
    cursor.execute(query1,(1,"abhi","indore"))
    con.commit()
    return "done"

@app.route("/showdata")
def showdata():
    query2 = ("select * from students")
    cursor = con.cursor()
    cursor.execute(query2)
    data = cursor.fetchall()
    return render_template("showdata.html",data = data)

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
        fur = request.form["furnishingstatus"]

        furnished = furnishing_encoder.transform([fur])[0]

        data = pd.DataFrame([[area, bathrooms, stories, parking,
                              airconditioning, furnished]],
                            columns=['area', 'bathrooms', 'stories', 'parking',
                                     'airconditioning', 'furnishingstatus'])

        result = model.predict(data)[0]

    return render_template("predict.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
