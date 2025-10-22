from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List,Dict,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Patient Name",description="Mention name of the patient same as on CNIC card")]
    age:int
    weight:float
    married:bool
    allergies:List[str] = Field(max_length=5)
    contact:Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergencies(cls, model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('Emergency Contact is not available')
        return model
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print("Data inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Data updated")


patient_info = {'name':'jamshed','age':'90','weight':23.3,'married':False,'allergies':['pollen','dust','smell','sdf','adff'],'contact':{'contact_number':'234234','email':'jamshed@gmail.com','emergency':'23342'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)