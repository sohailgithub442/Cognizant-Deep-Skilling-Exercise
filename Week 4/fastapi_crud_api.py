from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="Employee Management API",
    description="FastAPI demo with Pydantic Models and automatic OpenAPI documentation",
    version="1.0.0"
)

# Pydantic Model
class Employee(BaseModel):
    id: int = Field(..., gt=0, description="Employee ID")
    name: str = Field(..., min_length=3, max_length=50)
    department: str
    salary: float = Field(..., gt=0)

# In-memory database
employees: List[Employee] = []

# Home
@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}

# Get all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees

# Get employee by ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Add employee
@app.post("/employees", response_model=Employee, status_code=201)
def add_employee(employee: Employee):
    for emp in employees:
        if emp.id == employee.id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")
    employees.append(employee)
    return employee

# Update employee
@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees):
        if emp.id == emp_id:
            employees[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
