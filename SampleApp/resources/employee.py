from flask import request
from flask_restplus import Resource, fields, Namespace

from models.employee import EmployeeModal
from schemas.employee import EmployeeSchema

EMP_NOT_FOUND = "Employee not found."


employee_ns = Namespace('employee', description='Employee related operations')
employees_ns = Namespace('employees', description='Employees related operations')

employee_schema = EmployeeSchema()
employee_list_schema = EmployeeSchema(many=True)

#Model required by flask_restplus for expect
employee = employees_ns.model('Employee', {
    'employee_id': fields.String('Id of the Employee'),
    'name': fields.String('Name of the Employee'),
    'age':fields.Integer,
    'position':  fields.String('position of the Employee')
})


class Employee(Resource):

    def get(self, id):
        employee_data = EmployeeModal.find_by_id(id)
        if employee_data:
            return employee_schema.dump(employee_data)
        return {'message': EMP_NOT_FOUND}, 404

    def delete(self,id):
        employee_data = EmployeeModal.find_by_id(id)
        if employee_data:
            employee_data.delete_from_db()
            return {'message': "Item Deleted successfully"}, 200
        return {'message': EMP_NOT_FOUND}, 404

    @employee_ns.expect(employee)
    def put(self, id):
        employee_data = EmployeeModal.find_by_id(id)
        employee_json = request.get_json()

        if employee_data:
            employee_data.employee_id = employee_json['employee_id']
            employee_data.name = employee_json['name']
            employee_data.age = employee_json['age']
            employee_data.position = employee_json['position']          
        else:
            employee_data = employee_schema.load(employee_json)

        employee_data.save_to_db()
        return employee_schema.dump(employee_data), 200


class EmployeeList(Resource):
    @employees_ns.doc('Get all the Employees')
    def get(self):
        return employee_list_schema.dump(EmployeeModal.find_all()), 200

    @employees_ns.expect(employee)
    @employees_ns.doc('Create an Employee')
    def post(self):
        employee_json = request.get_json()
        employee_data = employee_schema.load(employee_json)
        employee_data.save_to_db()

        return employee_schema.dump(employee_data), 201
