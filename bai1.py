
students = []

n = int(input("Enter student number: "))

for i in range(n):
    print(f"\nEnter information for student {i + 1}:")

    student_id = input("Enter student ID: ")
    full_name = input("Enter full name: ")
    python_score = float(input("Enter Python score: "))

    student = {
        "student_id": student_id,
        "full_name": full_name,
        "python_score": python_score
    }

    students.append(student)

print("\n=== STUDENT LIST ===")

for student in students:
    print(f"Student ID: {student['student_id']}")
    print(f"Full Name: {student['full_name']}")
    print(f"Python Score: {student['python_score']}")
    print("--------------------")

if n > 0:
    max_student = students[0]

    for student in students:
        if student["python_score"] > max_student["python_score"]:
            max_student = student

    print("\n=== STUDENT WITH HIGHEST SCORE ===")
    print(f"Student ID: {max_student['student_id']}")
    print(f"Full Name: {max_student['full_name']}")
    print(f"Python Score: {max_student['python_score']}")

    total_score = 0

    for student in students:
        total_score += student["python_score"]

    average_score = total_score / len(students)

    print(f"\nAverage Score: {average_score:.2f}")

print("\n=== STUDENTS WHO PASSED ===")

for student in students:
    if student["python_score"] >= 5:
        print(f"{student['student_id']} - {student['full_name']} - {student['python_score']}")
