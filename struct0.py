from cs50 import get_string

students = []

for i in range(3):
    name = get_string("Name: ")
    dorm = get_string("Dorm: ")

    # Assign variables in hash table
    student = {"name": name, "dorm": dorm}

    strudents.append(student)

for student in students:
    print(f"{student['name']} is in this {student['dorm']}")