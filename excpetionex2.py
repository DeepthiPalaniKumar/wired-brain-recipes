stud={
    "name" : "Mark",
    "id":13,
    "feedback":None

}
stud["lastname"]="Kowsi"
try:
    lastname=stud["lastname"]
    numbered_lastname=3+lastname
except KeyError:
    print("Key eror is exempted")
except TypeError as error:
   print("Can't add two different data types")
   print(error)
#except Exception:
#    print("Caught all the exceptions")


print("This code executes")