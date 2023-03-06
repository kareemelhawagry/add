from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
