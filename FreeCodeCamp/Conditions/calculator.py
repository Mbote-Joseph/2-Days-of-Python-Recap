def calculator(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b
    else:
        return 'Invalid operator'

num1=int(input("Enter the first number: "))
op=input("Enter the operator: ")
num2=int(input("Enter the second number: "))


print(f"The result is {calculator(num1, num2, op)}")