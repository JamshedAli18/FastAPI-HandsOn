from pydantic import BaseModel, EmailStr, Field
from typing import List,Dict,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Patient Name",description="Mention name of the patient same as on CNIC card")]
    age:int
    weight:float
    married:bool
    allergies:List[str] = Field(max_length=5)
    contact:Dict[str, str]


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


patient_info = {'name':'jamshed','age':'30','weight':23.3,'married':False,'allergies':['pollen','dust','smell','sdf','adff'],'contact':{'number':'0323432','email':'jamshed@gmail.com'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
