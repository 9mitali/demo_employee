from flask import request, jsonify
from flask_restful import Resource
from db_config import get_db_connection
from models import EmployeeModel

conn = get_db_connection()

class Employee(Resource):
    def get(self, emp_id=None):
        
        if not conn:
            return {'message': 'Database connection failed'}, 500
        cursor = conn.cursor(dictionary=True)
        try:
            if emp_id:
                cursor.execute('SELECT * FROM em1 WHERE id_proof = %s', (emp_id,))
                employee = cursor.fetchone()
                if not employee:
                    return {'message': 'Employee not found'}, 404
                return jsonify(employee)
            else:
                cursor.execute('SELECT * FROM em1')
                employees = cursor.fetchall()
                return jsonify(employees)
        except Exception as e:
            print(f"Error during GET request: {e}")
            return {'message': 'Internal server error'}, 500

    def post(self):
        data = request.json
        if not data:
            return {'message': 'No input data provided'}, 400

        employee = EmployeeModel.from_dict(data)
        if not conn:
            return {'message': 'Database connection failed'}, 500
        cursor = conn.cursor()
        query = '''
            INSERT INTO em1 (Department, Name, Designation, Email, Address, location, DOB, DOJ, id_proof_type, id_proof, Gender, Phone, Country, Salary)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            employee.Department, employee.Name, employee.Designation, employee.Email, 
            employee.Address, employee.location, employee.DOB, employee.DOJ, 
            employee.id_proof_type, employee.id_proof, employee.Gender, 
            employee.Phone, employee.Country, employee.Salary
        )
        try:
            cursor.execute(query, values)
            conn.commit()
            return {'message': 'Employee added successfully'}, 201
        except Exception as e:
            print(f"Error adding employee: {e}")
            return {'message': 'Failed to add employee'}, 500

    def put(self, emp_id):
        data = request.json
        if not data:
            return {'message': 'No input data provided'}, 400

        employee = EmployeeModel.from_dict(data)
        if not conn:
            return {'message': 'Database connection failed'}, 500
        cursor = conn.cursor()
        query = '''
            UPDATE em1 
            SET Department=%s, Name=%s, Designation=%s, Email=%s, Address=%s, location=%s, 
                DOB=%s, DOJ=%s, id_proof_type=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s 
            WHERE id_proof=%s
        '''
        values = (
            employee.Department, employee.Name, employee.Designation, employee.Email, 
            employee.Address, employee.location, employee.DOB, employee.DOJ, 
            employee.id_proof_type, employee.Gender, employee.Phone, 
            employee.Country, employee.Salary, emp_id
        )
        try:
            cursor.execute(query, values)
            conn.commit()
            return {'message': 'Employee updated successfully'}, 200
        except Exception as e:
            print(f"Error updating employee: {e}")
            return {'message': 'Failed to update employee'}, 500

    def delete(self, emp_id):
        if not conn:
            return {'message': 'Database connection failed'}, 500
        cursor = conn.cursor()
        query = 'DELETE FROM em1 WHERE id_proof=%s'
        try:
            cursor.execute(query, (emp_id,))
            conn.commit()
            return {'message': 'Employee deleted successfully'}, 200
        except Exception as e:
            print(f"Error deleting employee: {e}")
            return {'message': 'Failed to delete employee'}, 500
