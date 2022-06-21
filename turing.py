t='%(a)s %(b)s %(c)s'

print(t %dict(a="welcome", b="to", c="Turinhg"))

# Y=[2,5J,6]
# Y.sort()
# print(Y)

a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0, len(a))]
print(b)

def f(x, l=[]):
    for i in range(x):
        l.append(i *i)
    print(l)

f(2)
f(3, [3,2,1])
f(3)

z=set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)

l=[1,2,3,4,5]
m=map(lambda x:2**x, l)
print(list(m))

def listskills(val, list=[]):
    list.append(val)
    return list

list1= listskills("NodeJS")
list2 = listskills("Java", [])
list3= listskills("JavaScript")
print(list1, list2, list3)

print("Welcome to TURING".capitalize())

data=[1,2,3]
def incr(x):
    return x + 1

print(list(map(incr, data)))

# x= "abcdef"
# i="a"

# while i in x[:1]:
#     print(i, end=" ")

from copy import copy
import re
result= re.findall('Welcome to Turing', 'Welcome',1)
print(result)

data=['a','b','c']
newlist=copy(data)
print(newlist)

print(2**(3**2), (2**3)**2, (2**3)**3)

print([i.lower() for i in "TURING"])

array1=[1,2,3,4,5]
array2=array1
array2[0]=0
print(array1)

list1=[1,2,6,12]
list2=[12,6,2,1]
print(list1==list2)
print(set(list1)==set(list2))