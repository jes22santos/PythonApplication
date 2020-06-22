from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/say-bye')
def say_bye():
  return 'Goodbye!'

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug = True, port = os.environ.get('PORT')) 