# Student Qualification App
# Author: Tadelo Jember
# File Name: student_qualification.py
# Description: This app accepts student names and GPAs and determines if the student qualifies for the Dean's List or the Honor Roll.
# Initialize an empty list to store student records


student_records = []
# Main loop to input student information
while True:
    last_name = input("Enter student's last name (type 'ZZZ' to quit): ").upper()
   
    if last_name == 'ZZZ':
        break
   
    first_name = input("Enter student's first name: ").upper()
    gpa = float(input("Enter student's GPA: "))
   
    student_records.append((first_name, last_name, gpa))

# Check the qualification for each student
for student in student_records:
    if student[2] >= 3.5:
        print(f"{student[0].capitalize()} {student[1].capitalize()} has made the Dean's List.")
    elif student[2] >= 3.25:
        print(f"{student[0].capitalize()} {student[1].capitalize()} has made the Honor Roll.")
    else:
        print(f"{student[0].capitalize()} {student[1].capitalize()} does not qualify for any honors.")

# End of the program
print("Program completed.")