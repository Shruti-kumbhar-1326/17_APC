#5.	Create a list of student names. Remove:
#•	First student 
#•#	Last student 
#•	A specific student by name  
#Display the remaining list.

students =["shruti","prachi" ,"siddhi","vaishnvi","kalyani"]
print("original list of student name:",students)
students.pop(0)
print("remove first name:",students)
students.pop()
print("remove last name:",students)
name = input("enter a name to remove :")
if name in students:
    students.remove(name)
else :
    print("student not found:")
print("remaining student name",students)        
