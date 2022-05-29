teams =["Chelsea", "Manchester United", "Manchester City", "Arsenal", "Tottenham"]

for team in teams:
    print(f"{team} is a great team!")

# Another design pattern is the for loop.
# The for loop is used to iterate over a sequence of items,
# and it is also used to iterate over the members of an object.
print("\n===========================================\n")
for i in range(len(teams)):
    print(f"{teams[i]} is a great team!")

print("\n===========================================\n")

for letters in "Hello":
    print(letters)

print("\n===========================================\n")

for index in range(3,10):
    print(index)