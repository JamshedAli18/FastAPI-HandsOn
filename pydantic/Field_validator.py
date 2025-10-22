from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from typing import List,Dict,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Patient Name",description="Mention name of the patient same as on CNIC card")]
    age:int
    weight:float
    married:bool
    allergies:List[str] = Field(max_length=5)
    contact:Dict[str, str]
    email:EmailStr

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['muet.com','muetkhp.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValidationError('Invalid email address')
        return value

    @field_validator('name')
    @classmethod
    def Capitalize_name(cls, value):
        return value.upper()

def insert_patient_data(patient: Patient):

    print(patient.email)

    print("Data inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print(patient.email)
    print("Data updated")


patient_info = {'name':'jamshed','age':'30','weight':23.3,'married':False,'allergies':['pollen','dust','smell','sdf','adff'],'contact':{'number':'0323432','address':'jamshed@gmail.com'},'email':'jamshed@muet.com'}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)

