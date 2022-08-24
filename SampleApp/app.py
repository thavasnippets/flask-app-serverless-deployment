from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db
from resources.employee import Employee, EmployeeList, employee_ns, employees_ns
from marshmallow import ValidationError

app = Flask(__name__)
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, doc='/doc', title='Sample Application')
app.register_blueprint(bluePrint)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123!@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


api.add_namespace(employee_ns)
api.add_namespace(employees_ns)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

employee_ns.add_resource(Employee, '/<int:id>')
employees_ns.add_resource(EmployeeList, "")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run()
