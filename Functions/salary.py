Employees={
    'A':{'name':'Aggie','salary':1000},
    'B':{'name':'Ben','salary':2000},
    'C':{'name':'Clara','salary':3000},
    'D':{'name':'Dapph','salary':4000},
    'E':{'name':'Egline','salary':5000},
}

def increase_salary(employees):
    for employee in employees:
        if employees[employee]['salary']<5000:
            employees[employee]['salary']+=1000
    return employees

def print_salary(employees):
    for employee in employees:
        print(f"{employees[employee]['name']}'s salary is {employees[employee]['salary']}")

increase_salary(Employees)

print("\n===============Employees Salary List===============")
print_salary(Employees)