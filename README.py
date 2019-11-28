from flask import flask
app= flask(_name_)
@app.router('/')
def hola_mundo():
return 'Hey its python flask application!'
if_name_=='_main_':
app.run()
