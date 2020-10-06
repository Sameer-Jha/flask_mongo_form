from flask import Flask, render_template, request
import hashlib
from db_ops import db

app = Flask(__name__)
database = db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        result = dict(request.form)
        result['password'] = hashlib.md5(result['password'].encode('utf-8')).hexdigest()
        database.store_data(result)
        return render_template("results.html", result=result)

@app.route('/data')
def data():
    data = database.retrieve_data()
    keys = data[0].keys()
    return render_template('data.html', data=data, keys=keys)

@app.route('/docs')
def docs():
    return render_template('docs.html')


if __name__ == "__main__":
    app.run(debug=True)