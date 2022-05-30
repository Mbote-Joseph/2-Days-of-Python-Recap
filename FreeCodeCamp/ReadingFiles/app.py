# employee_file = open("employees.txt", "r")
# print(employee_file.readable())

# employee_file.close()
# try:
#     employee_file = open("employees.txt", "r")
#     print(employee_file.readable())
# except FileNotFoundError:
#     print("The file is not found.") 
employee_file = open("employees.txt", "r")
# employee_file.write("Jim - Salesman \n Dwight- Salesman \n Angela - Salesman \n Pam - Receptionist \n Michael - Manager \n Oscar - Accountant")
print(employee_file.readable())
print(employee_file.read())
print("===========================================")
print("Reading line by line")
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)


employee_file.close()