# Lambda Functions
def details (a,b,c):
     print(f'my name is {a}')
     print(f'my calss is {b}')
     print(f'my roll is {c}')
details('srav',5,'5A')
print()
details(c='5A',a='srav',b='5')
print()
def add (a,b=100,c=200):
    print(a + b + c)
add (10)
add(10,30)
add(10,20,30)
add(10,20,c=30) # must need in =
print()
def add (a, *b):
    print(b)
add(1, 2,3,4,5,6,7,8,9)

def add (a, **b):
    print(b)
add(1,x=2, y=3, z=4, j=9,m=5,h=8)
print()

a= 10     # visible for entire file
def display():
    b=20   #visible to only this function
    print(a,b)
display()
print()
# global keyword
a= 10     
def display():
    global a # treat  a as  global varibale
    a=20   
display()
print(a)
print()
# call by value # call by reference
def display(a):
    print(a)
display(20)  # call by values
b=[1,2,3,4,5]
display(b)  # call by reference 
print()
# lambda
a= lambda x,y : x+y
print(a(10,30))




# Lambda Functions
#1. Program to write lambda function to take x and return x^2
x = 10
res = lambda x: x ** 2
print(res(x))
# or 
print((lambda x: x ** 2)(x))

a = 5
#2. Program to write lambda function to take x and return its sum
total = lambda a: sum(range(1, a + 1)) 
print(total(a))
#or
total = lambda a: a * (a + 1) // 2
print(total(a))

#3. Program to write lambda function to take sequence and return second element of it
arr = [2, 4, 6, 8, 10]
ele = lambda arr: arr[1]
print(ele(arr))

#4. Program to write lambda function to take list and return its sum
arr = [2, 4, 6, 8, 10]
total = 0
arr_sum = lambda arr: sum(arr)
print(arr_sum(arr))
# or 
from functools import reduce
arr = [2, 4, 6, 8, 10]
total = 0
arr_sum = reduce(lambda x, y: x + y, arr)
print(arr_sum)

arr_sum = lambda arr: reduce(lambda x, y: x + y, arr)
print(arr_sum(arr))
