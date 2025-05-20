from fastapi import FastAPI, HTTPException, StatusCode
from pydontic import BaseModel, sqla_model
from sqlachemy import Column, Integer, String

app = FastAPI()

class Employee(BaseModel):
    id: Integer
    name: String
    age: Integer
    position: String

@app.get("/employees")
def read_employees():
    # Read all employees from database
    pass

@app.post("/employees")
def create_employee(employee: Employee):
    # Create new employee in database
    pass

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    # Update existing employee in database
    pass

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: Integer):
    # Delete existing employee from database
    pass
