x= int(input('Enter a number: '))
y= int(input('Enter a number: '))

try:
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
