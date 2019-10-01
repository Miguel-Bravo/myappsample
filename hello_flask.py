from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

TRUTHY = ['true', 'True', 'yes']

class HelloWorld(Resource):
	def get(self):

		with open('data.txt') as json_file:
			data = json.load(json_file)

			print('Encendido: ' + str(data['encendido']))
			print('Duracion: ' + str(data['duracion']))
			print('')

		return {'Encendido': data['encendido'],
				'Duracion': data['duracion']}

	def post(self):
		some_json =request.get_json()
		return {'you sent': some_json}, 201


class Mod(Resource):
	def get(self):
		# Get `class` list from request args
		#classes = request.args.getlist('class')
		duracion = int(request.args.get('duracion'))

		#Get `encendido` boolean from request args
		encendido = True if request.args.get('encendido') in TRUTHY else False

		if duracion < 0:
			duracion = 0

		data = {
			'encendido': encendido,
			'duracion': duracion
		}

		with open('data.txt', 'w') as outfile:
			json.dump(data, outfile)

		return {'Duracion': duracion, 'Encendido': encendido}

api.add_resource(HelloWorld, '/')
api.add_resource(Mod, '/mod')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
