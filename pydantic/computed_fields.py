from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError,computed_field
from typing import List,Dict,Annotated

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def BMI(self) -> float:
        bmi = round(self.weight / (self.height * self.height),3)
        return bmi


def insert_patient_data(patient: Patient):
    print(patient.weight)
    print(patient.height)
    print(patient.BMI)


def update_patient_data(patient: Patient):
    pass


patient_info = {'weight':23.23,'height':45.22}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)

