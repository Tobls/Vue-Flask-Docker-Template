from flask import render_template

from server import app

@app.route('/api/helloworld', methods=['GET', 'POST'])
def hello_world():
    return "Hello, World", 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template('index.html')
