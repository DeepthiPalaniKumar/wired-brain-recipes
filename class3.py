students=[]

class Student:

    school_name="Springfield Elementary"

    def __init__(self,name, student_id=332):
        self.name=name
        self.student_id=student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_schn(self):
        return self.school_name


mark=Student("Tim",220)

#student=Student()
#student.add_stud("Mark")
print(mark)
print(students)
print(Student.school_name)

