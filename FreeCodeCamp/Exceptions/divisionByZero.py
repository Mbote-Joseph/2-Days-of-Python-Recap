x = int(input("Enter a number: "))
y = int(input("Divide By: "))

try: 
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError:
    print("You can't divide by zero!")