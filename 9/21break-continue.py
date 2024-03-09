#break and continue
students = ["ram", "shyam", "ziva", "priya","suraj"]
for student in students:
    if student == "priya":
        break;
    print(student)
print("......\n")

for leave_student in students:
    if leave_student == "priya":
        continue;
    print(leave_student)