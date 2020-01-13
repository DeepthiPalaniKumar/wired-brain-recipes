students=[]

class Student:
    def __init__(self,name, stud_id=332):
        student = {"name": name, "sudent_id": stud_id}
        students.append(student)

    def __str__(self):
        return "Student"
       # print(student)
mark=Student("Tim",220)

#student=Student()
#student.add_stud("Mark")
print(mark)
print(students)

