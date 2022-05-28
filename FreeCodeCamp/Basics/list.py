friends = [ "Kevin", "Karen", "Jim","Aggie","Juma", "Oscar", "Toby"]
print(friends[0])
print(friends[-1])
print(friends[1:3])

friends[1 : 3] = ["Mark", "Tom"]
print(friends[:])

print(friends.index("Oscar"))
print(friends.count("Oscar"))
print(friends.append("Oscar"))