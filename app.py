# from flask import Flask, render_template, request

# app = Flask(__name__,)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/success", methods=['POST'])
# def success():
#     if request.method=='POST':
#         email=request.form["email_name"]
#         name=request.form["name_name"]
#         age=request.form["age_name"]
#         height=request.form["height_name"]
#         weight=request.form["weight_name"]
#         print(email, name, age, height, weight)
#         return render_template("success.html")

# if __name__ == '__main__':
#     app.debug=True
#     app.run(debug=True, use_reloader=True)
#-----------------------------------------------------

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/app', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']

    if weight and height:
        y = int(weight)
        x = int(height)
        z = y/(x*x/10000)
        newName = round(z,1)
        return jsonify({'name' : newName})

    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)