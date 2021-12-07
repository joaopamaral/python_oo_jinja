"""https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf"""
from flask import Flask, request, render_template, jsonify
from src.Day3.jinja_example import InfraJinja

app = Flask(__name__)


@app.route("/")
def simple_get():
    return "<p>Hello, World!</p>"


@app.route('/hello/<string:name>')
def get_with_parameter(name):
    return 'Hello ' + name + '!'


@app.route('/test', methods=['GET', 'POST'])
def get_and_post():
    if request.method == 'GET':
        return 'You sent a GET request'
    elif request.method == 'POST':
        return f'You sent a POST request! Payload {request.form}'


@app.route('/infra')
def infra_jinja_template():
    return render_template('infra.template', infras=[
        InfraJinja('infra1', 'aws'),
        InfraJinja('infra2', 'gcp'),
        InfraJinja('infra3', 'azure')
    ])


@app.route('/return_json')
def return_json():
    num_list = [1, 2, 3, 4, 5]
    num_dict = {'numbers' : num_list, 'name' : 'Numbers'}
    # returns {'output' : {'numbers' : [1,2,3,4,5], 'name' : 'Numbers'}}
    return jsonify({'output': num_dict})


if __name__ == '__main__':
    app.run(debug=True)