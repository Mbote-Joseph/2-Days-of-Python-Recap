from Graduation import Student

student1 = Student("Anna", "MIT", 3.5)
student2 = Student("Bob", "MIT", 3.0)
student3 = Student("Cathy", "MIT", 2.5)
student4 = Student("David", "MIT", 2.0)
student5 = Student("Eve", "MIT", 1.5)

students = [student1, student2, student3, student4, student5]

for student in students:
    graduation_list = open("graduation_list.txt", "a")
    graduation_list.write(str(student) + "\n")
    graduation_list.close()
    print(student)
