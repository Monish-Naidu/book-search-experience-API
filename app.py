
from flask import Flask, app
from flask_restplus import Api, Resource
#app = Flask(__name__)
api = Api(app)

#@app.route('/')
#def hello_world():
#    return 'We are Team Goat'
if __name__ == '__main__':
    app.run(debug = True)  #starting a development server
