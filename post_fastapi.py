import json
from fastapi import FastAPI,HTTPException,Path,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,computed_field,Field
from typing import Optional,Annotated,Literal

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str,Field(...,description="Patient ID",examples=["P001"])]
    name: Annotated[str,Field(...,description="Patient Name",examples=["Jamshed"])]
    age: Annotated[int,Field(...,description="Patient Age should be in this range(18,50)",gt=18,le=50)]
    city: Annotated[str,Field(..., description="City from where you belong",examples=["Mumbai"])]
    gender: Annotated[Literal['male','female',"others"],Field(...,description="Gender of Patient")]
    height: Annotated[float,Field(...,description="Height of the patient in meters")]
    weight: Annotated[float,Field(...,description="Weight of the patient in kilograms")]

    @computed_field()
    @property
    def bmi(self) -> float:
        bmi = self.weight/(self.height**2)
        return bmi

    @computed_field()
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        else:
            return "Overweight"


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.post("/create")
def create_patient(patient: Patient):

    # load JSON data
    data = load_data()

    # checks if that is already availble or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # new patient data add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})
