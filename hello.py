#import flask
from flask import Flask
app=Flask(__name__)
@app.route ('/')
def hello_world():
    return "<div><h1>Hello world</h1><br><h1>hai</div>"
if __name__=='__main__':
    app.run(debug=True)