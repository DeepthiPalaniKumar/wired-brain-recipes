students=[]

def get_student_titlecase():
    stud_titlecase=[]
    for stud in students:
        stud_titlecase=stud.title()
    return stud_titlecase


def print_stud_titlecase():
    stud_titlecase=get_student_titlecase()
    print(stud_titlecase)


def add_stud(name,stud_id=332):
    student={"name":name,"sudent_id":stud_id}
    students.append(student)


def var_args(name,*args):   #it is only a list and not a dictionay as it does not have the ey for its value
    print(name)
    print(args)

add_stud(name="Mark",stud_id=15)



def keyword_args(nam,**kwargs):     #this is a dictionary as it has key and value where kwargs is used as key i.e. descirpion
    print(nam)
    print(kwargs["description"],kwargs["feedback"])

var_args("Tom","loves python",3,None,True)

keyword_args("Lili",description="Loves python",feedback=None,pluralsight_subscribe=True)

