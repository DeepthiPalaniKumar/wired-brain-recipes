stud={
    "name" : "Mark",
    "id":13,
    "feedback":None

}
try:
    last_name=stud["lastname"]
except KeyError:
    print("Key eror is exempted")


print("This code executes")