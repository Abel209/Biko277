from flask import flask
app = flask(__name__)
@app.router("/")
def hola_mundo():
return "hola munda mi nombre es abel"
