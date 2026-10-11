students = []
for i in range(5):
    student = {
        "name": input("enter the name of student : "),
        "rollno": input("enter the roll number of student : "),
        "python": int(input("enter the marks of python : ")),
        "ai": int(input("enter the marks of ai : ")),
        "maths": int(input("enter the marks of maths : "))
    }
    students.append(student)

def calculate_results(student):
    total_marks = student["python"] + student["ai"] + student["maths"]
    percentage = (total_marks / 300) * 100
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total_marks, percentage, grade

file = open("results.txt", "w")
file.write("Students results:\n")
file.write("Name\tRollno\tTotal marks\tPercentage\tGrade\n")

highest_percentage = 0
highest_student = ""

for student in students:
    total_marks, percentage, grade = calculate_results(student)

    print("Name:", student["name"], "Roll No:", student["rollno"],
          "Total Marks:", total_marks, "Percentage:", round(percentage, 2), "Grade:", grade)

    file.write(student["name"] + "\t" + student["rollno"] + "\t"
               + str(total_marks) + "\t" + str(round(percentage, 2)) + "\t" + grade + "\n")

    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_student = student["name"]

print("highest student:", highest_student, "having", (highest_percentage ), "%")
file.write("Highest student: " + highest_student + " having " + str(highest_percentage) + "\n")

file.close()

