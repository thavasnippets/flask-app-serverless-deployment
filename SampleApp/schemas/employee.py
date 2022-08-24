from ma import ma
from models.employee import EmployeeModal



class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeModal
        load_instance = True