from flask import Blueprint

maestros = Blueprint('maestros', __name__)

@maestros.route('/getMaestros', methods=['GET'])
def getMaestros():
    return {'Key':'Maestros'}