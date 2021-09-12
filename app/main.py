from flask import Flask
from flask import request

from data import Data

data = Data()
app = Flask(__name__)

@app.route('/geonameid/<int:geonameid>', methods=['GET'])
def geonameid(geonameid:int):
    return data.getById(geonameid) 

@app.route('/comparison', methods=['GET'])
def comparison():
    response = {}

    city1 = data.getByRusName(request.args.get('city1', ''))
    city2 = data.getByRusName(request.args.get('city2', ''))

    if not city1 and not city2:
        return response

    response['north'] = city1.get('name', 0) if city1.get('lat', 0) >= city2.get('lat', 0) else city2.get('name', 0)
    response['timezone'] = 'yes' if city1.get('timezone', '') == city2.get('timezone', '') else 'no'

    return response

@app.route('/help/city/<string:city>', methods=['GET'])
def helpCity(city:str):
    return data.getByNameContains(city)


@app.route('/page/<int:page>', methods=['GET'])
def page(page:int):
    quantity = request.args.get('quantity', 0)
    return data.getPage(page, int(quantity))

if __name__ == '__main__':
    app.run(debug=True, port='4000')
