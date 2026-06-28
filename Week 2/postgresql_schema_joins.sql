-- Create Department Table
CREATE TABLE Department (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Create Employee Table
CREATE TABLE Employee (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Insert Data
INSERT INTO Department (dept_name)
VALUES
('HR'),
('IT'),
('Finance');

INSERT INTO Employee (emp_name, salary, dept_id)
VALUES
('Alice', 50000, 1),
('Bob', 60000, 2),
('Charlie', 55000, 2),
('David', 70000, 3);

-- INNER JOIN
SELECT
    Employee.emp_name,
    Department.dept_name
FROM Employee
INNER JOIN Department
ON Employee.dept_id = Department.dept_id;
