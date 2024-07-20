from flask import Blueprint, request, jsonify
from app import db
from .models import Employee

main = Blueprint('main', _name_)

@main.route('/')
def home():
    return "WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM"

@main.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_emp = Employee(name=data['name'], position=data['position'], salary=data['salary'])
    db.session.add(new_emp)
    db.session.commit()
    return jsonify(new_emp.to_dict()), 201

@main.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': f"Employee with id {employee_id} not found!"}), 404
    return jsonify(employee.to_dict())

@main.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': "Employee not found"}), 404
    data = request.get_json()
    employee.name = data['name']
    employee.position = data['position']
    employee.salary = data['salary']
    db.session.commit()
    return jsonify({'message': "Employee updated successfully"})

@main.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': "Employee not found"}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': "Employee deleted successfully"})from flask import Blueprint, request, jsonify
from app import db
from .models import Employee

main = Blueprint('main', _name_)

@main.route('/')
def home():
    return "WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM"

@main.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_emp = Employee(name=data['name'], position=data['position'], salary=data['salary'])
    db.session.add(new_emp)
    db.session.commit()
    return jsonify(new_emp.to_dict()), 201

@main.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': f"Employee with id {employee_id} not found!"}), 404
    return jsonify(employee.to_dict())

@main.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': "Employee not found"}), 404
    data = request.get_json()
    employee.name = data['name']
    employee.position = data['position']
    employee.salary = data['salary']
    db.session.commit()
    return jsonify({'message': "Employee updated successfully"})

@main.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': "Employee not found"}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': "Employee deleted successfully"})