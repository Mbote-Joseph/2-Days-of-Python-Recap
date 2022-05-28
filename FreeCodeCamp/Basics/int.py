#I=PRT/100
principal= int(input("Enter the principal amount: "))
rate= int(input("Enter the rate of interest: "))
time= int(input("Enter the time in years: "))

interest= (principal*rate*time)/100
print(f"The interest is {interest}")

amount= principal+interest
print(f"The amount is {amount}")



