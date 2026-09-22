students = {
    101: ("Alice", "CSE", [85, 90, 88]),
    102: ("Bob", "ECE", [78, 82, 80]),
    103: ("Charlie", "ME", [92, 89, 95])
}

students[104] = ("Diana", "IT", [88, 79, 91])

del students[102]

students[101] = ("Alice", "CSE", [90, 92, 95])

print("Final Student Records:")
for roll_no, details in students.items():
    name, branch, marks = details
    print(f"Roll Number: {roll_no}, Name: {name}, Branch: {branch}, Marks: {marks}")