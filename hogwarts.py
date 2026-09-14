students = ["Harry", "Hermione", "Ron"]
print(students[0])  # Harry
print(students[1])  # Hermione
print(students[2])  # Ron  
#Another way to do this is:
for student in students:
    print(student)
#other way to print this is:
for i in range(len(students)):
    print(i + 1, students[i])
#Using dictionaries to store student information
students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag", "year": 5},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter", "year": 5},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier", "year": 5},
    {"name": "Draco", "house": "Slytherin", "patronus": None, "year": 5}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], student["year"], sep=", ")
