import flask
from Alumnos.routes import alumnos
from Maestros.routes import maestros
from Directivos.routes import directivos

app=flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home", methods = ['GET'])
def home():
    return flask.jsonify({'principal':'HOME'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()