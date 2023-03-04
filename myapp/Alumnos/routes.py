from flask import Blueprint

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getAlumnos', methods=['GET'])
def getAlumnos():
    return {'Key':'Alumnos'}