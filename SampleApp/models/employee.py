from db import db
from typing import List

class EmployeeModal(db.Model):
    __tablename__ = "Employee"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return 'EmployeeModal(employee_id=%s, name=%s,age=%s,position=%s )' % (self.employee_id, self.name,self.age,self.position)
    
    def json(self):
        return {'employee_id': self.name, 'name': self.name, 'age':self.age, 'position':self.position}
    
    @classmethod
    def find_by_name(cls, name) -> "EmployeeModal":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "EmployeeModal":
        return cls.query.filter_by(employee_id=_id).first()

    @classmethod
    def find_all(cls) -> List["EmployeeModal"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
