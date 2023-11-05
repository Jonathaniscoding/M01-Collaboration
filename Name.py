###Case Study: if... else and while
#Jonathan Engle
#Name.py
#Will accept users inputed first and last name of a student as well as their GPA. It will then sort the added GPAs into honor roll and deans list discarding those that failed to make the cut.
#it will then print those two lists.
Students ={}
Student_Deans_List = []
Student_Honor_Roll = []

while True:
    last_name = input("Please enter the Students last name: ")
    if last_name =="ZZZ":
        break
    first_Name = input("Please enter the Students First name: ")
    gpa = float(input("Please enter the Students GPA: "))
    Student_Info = {"First name": first_Name, "Last Name": last_name, "GPA": gpa}
    Students[last_name] = Student_Info



for student in Students.values():
    if student['GPA'] >= 3.5 and student['GPA'] < 4.0:
        Student_Honor_Roll.append(student)
    elif student['GPA'] >= 4.0:
        Student_Deans_List.append(student)

tudent_Deans_List = sorted(Student_Deans_List, key=lambda x: x['GPA'], reverse=True)
Student_Honor_Roll = sorted(Student_Honor_Roll, key=lambda x: x['GPA'], reverse=True)

print("The following students have made the Dean's List:")
for student in Student_Deans_List:
    print(f"{student['First name']} {student['Last Name']} (GPA: {student['GPA']})")

print("The following students have made the Honor Roll:")
for student in Student_Honor_Roll:
    print(f"{student['First name']} {student['Last Name']} (GPA: {student['GPA']})")