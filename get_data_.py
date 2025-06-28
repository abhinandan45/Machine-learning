import pandas as pd
import joblib
import pymysql
import pymysql.cursors
from flask import Flask,render_template,request

con = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="flask",
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html') 


@app.route("/upload",methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file)

    cursor = con.cursor()
    create_table = ''' create table houseone
    (price int , area int , bedrooms int , 
    bathrooms int , stories int , 
    mainroad varchar(5), guestroom varchar(4),
    basement varchar(5), hotwatering varchar(5) 
    ,airconditioning varchar(5), parking int ,
    prefarea varchar(5) , 
    furnishingstatus varchar(30) )

'''
    cursor.execute(create_table)
    con.commit()
    
    inser_table = """       
    insert into house(price , area, bedrooms , 
    bathrooms , stories , 
    mainroad, guestroom,
    basement, hotwatering  
    ,airconditioning , parking,
    prefarea , furnishingstatus
    )
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)


"""

    for _, row in df.iterrows():
        cursor.execute(inser_table,tuple(row))


    con.commit()
    cursor.close()
    con.close()

    return "data uploaded"

if __name__ == "__main__":
    app.run(debug=True)







