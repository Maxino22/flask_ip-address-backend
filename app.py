from flask import Flask, render_template, make_response, Response
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS
import requests


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


@api.route('/api')
class IpApi(Resource):
    # get ip address
    parse = reqparse.RequestParser()
    parse.add_argument('ip_address',
                       type=str,
                       required=True,)

    # access current data                   help='Must add an IP')
    def get(self):
        r = requests.get('https://api.ipify.org/')
        return r.text

    # to get entered values
    def post(self):
        data = IpApi.parse.parse_args()

        response = requests.get(
            f'https://geo.ipify.org/api/v1?apiKey=at_38eFIk7s4ElmCDNeKcn3nO2zD9E5u&ipAddress={data["ip_address"]}')

        return response.json()


if __name__ == '__main__':
    app.run(debug=True)
