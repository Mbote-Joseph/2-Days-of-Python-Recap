isMale= True
isTall= False

if isMale and isTall:
    print("You are a tall and you are tall")

elif isMale and not(isTall):
    print("You are a short and you are a male")

elif not(isMale) and isTall:
    print("You are not a male and you are tall")

elif not(isMale) and not(isTall):
    print("You are not either tall nor male")

else:
    print("I am not sure about you !")