students=[]

class Student:

    school_name="Springfield Elementary"

    def __init__(self,name, student_id=332):
        self.name=name
        self.student_id=student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def gt_namecapitalize(self):
        return self.name.capitalize()


    def get_schn(self):
        return self.school_name

class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    def get_schn(self):
        return " This is a high school student"

    def gt_namecapitalize(self):
        original=super().gt_namecapitalize()
        return original+"-HS-"

james=HighSchoolStudent("james")
print(james.gt_namecapitalize())
print(james.get_schn())

