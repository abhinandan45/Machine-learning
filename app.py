from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    data1 = 55
    return render_template("home.html", data1=data1)

@app.route("/about")
def about():
    data = [1, 2, 3, 4, 5, 6, 7, 6]
    return render_template("about.html", data=data)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/subform", methods=['POST'])
def subform():
    if request.method == 'POST':
        name = request.form['nm']
        number = request.form['number']  
        email = request.form['email']
        return render_template("form.html", formname=name, formnum=number,formemail=email)
    else:
        return "Form not submitted properly....."

if __name__ == "__main__":
    app.run(debug=True)


