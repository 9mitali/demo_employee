
from flask import Flask
from flask_restful import Api
from resources import Employee
import configparser


config = configparser.ConfigParser()
config.read('app.properties')


app = Flask(__name__)
api = Api(app)
                            
api.add_resource(Employee, '/employee', '/employee/<string:emp_id>')

if __name__ == '__main__':
    app.run(host=config['FLASK']['host'], port=int(config['FLASK']['port']),debug=TRUE)
    
