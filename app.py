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
        new = round(z,1)
        return jsonify({'name' : new})

    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)