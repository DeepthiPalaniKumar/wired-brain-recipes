students=[]

def get_student_titlecase():
    stud_titlecase=[]
    for stud in students:
        stud_titlecase.append(stud["name"].title())
    return stud_titlecase


def print_stud_titlecase():
    stud_titlecase=get_student_titlecase()
    print(stud_titlecase)


def add_stud(name,stud_id=332):
    student={"name":name,"sudent_id":stud_id}
    students.append(student)


def save_file(student):
    try:
        f=open("stu.txt","a")
        f.write(student+"\n")
        f.close()
    except Exception:
        print("Could no save file")


def read_file():
    try:
        f=open("stu.txt","r")
        for student in f.readlines():
            add_stud(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_stud_titlecase()

studn=input("Enter the student name: ")
studid=input("Enter the student ID:")

add_stud(studn,studid)
save_file(studn)



