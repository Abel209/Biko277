from flask import flask
app = flask(__name__)
@app.router('/')
def hola_mundo():
return 'Hey its python flask application!'
if__name__=='__main__':
app.run()
