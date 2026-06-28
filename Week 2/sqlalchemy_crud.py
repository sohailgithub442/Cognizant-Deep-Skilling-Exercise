from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Connection
engine = create_engine("sqlite:///students.db")

Base = declarative_base()

# Table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)

# Create Table
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# CREATE
student = Student(name="Alice", department="CSE")
session.add(student)
session.commit()

# READ
print("Students:")
for s in session.query(Student).all():
    print(s.id, s.name, s.department)

# UPDATE
student = session.query(Student).filter_by(name="Alice").first()
student.department = "IT"
session.commit()

# DELETE
student = session.query(Student).filter_by(name="Alice").first()
session.delete(student)
session.commit()

print("CRUD Operations Completed Successfully.")
