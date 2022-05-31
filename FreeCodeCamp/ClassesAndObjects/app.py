from Student import Student

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(95)
anna.marks.append(71)
print(anna.marks)
print(anna.name)

print(f"Anna's average is {anna.average()}")