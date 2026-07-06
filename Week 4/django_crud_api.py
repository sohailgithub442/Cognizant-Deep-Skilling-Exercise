from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Sample Data
students = [
    {"id": 1, "name": "Alice", "department": "CSE"},
    {"id": 2, "name": "Bob", "department": "ECE"},
]

# CREATE & READ
@api_view(["GET", "POST"])
def student_list(request):

    if request.method == "GET":
        return Response(students)

    if request.method == "POST":
        students.append(request.data)
        return Response({"message": "Student Added"})


# UPDATE & DELETE
@api_view(["PUT", "DELETE"])
def student_detail(request, id):

    for student in students:

        if student["id"] == id:

            if request.method == "PUT":
                student["name"] = request.data["name"]
                student["department"] = request.data["department"]
                return Response({"message": "Student Updated"})

            if request.method == "DELETE":
                students.remove(student)
                return Response({"message": "Student Deleted"})

    return Response({"message": "Student Not Found"})


# URL Routing
urlpatterns = [
    path("students/", student_list),
    path("students/<int:id>/", student_detail),
]
