#I=PRT/100
principal= float(input("Enter the principal amount: "))
rate= float(input("Enter the rate of interest: "))
time= float(input("Enter the time in years: "))

interest= (principal*rate*time)/100
print(f"The interest is {interest}")

amount= principal+interest
print(f"The amount is {amount}")



