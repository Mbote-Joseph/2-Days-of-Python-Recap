employee_file = open("employees.txt", "a")
name=input("Enter name and Department: ")
employee_file.write("\n"+name)