employee_file = open("employees1.txt", "w")
name=input("Enter name and Department: ")
employee_file.write("\n"+name)
employee_file.close()