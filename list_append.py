
# way 1

print("Appending to a list")

arr=list()

print("How many elements are there in the list?")

e=int(input())

print("Enter the elements you would like to append to the empty list arr:")

s=input()

for i in range(e):
    arr.append(s[i])

print(arr)

# way 2

arr2=[1,2,3]

# way 3 

print("list using input()")

print("Enter the elements of the list a:")
a = [int(x) for x in input().split()]
#s=input()
#list2=list(map(int, s.split()))

print("List a is :")

print(a)

# way 4 

print("Enter the elements of the list b:")

s=input()
b=list(map(int, s.split()))

print("List b is :")

print(b)

# Extend 

print("Now Extend operator")

print("Enter the first list a:")

s=input()

a=list(map(int,s.split()))

print("Enter the second list b:")

s=input()

b=list(map(int,s.split()))


a.extend(b)

print("The merged list is :")
print(a)
    
# insert(i,x) 

print("Now insert(i,x)")

print("Given list a is :")

print(a)

print("Enter the number you would like to add:")

x=input()

print("Enter the position in the list you would like to add:")

p=int(input())

l=len(a)

if p>= l:
    print("Please enter a value from 0 to", l-1)
    p=int(input())
else:
    a.insert(p,x)

print("New list is :") 

print(a) 
    
    