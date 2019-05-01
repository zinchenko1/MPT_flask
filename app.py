from flask import Flask, render_template, request

app = Flask(__name__,)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        name=request.form["name_name"]
        age=request.form["age_name"]
        height=request.form["height_name"]
        weight=request.form["weight_name"]
        print(email, name, age, height, weight)
        return render_template("success.html")

if __name__ == '__main__':
    app.debug=True
    app.run(debug=True, use_reloader=True)