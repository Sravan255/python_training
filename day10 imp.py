#important problems
#1. print numbers from 1 to 10 
for x in range(1,11):
    print(x, end=' ')
print('\n\n')

#2. print even numbers from 5 to 30 and above list
list=[4,5,3,2,6,3,8,9,4,5,7,2,6,8]
for x in range(5,30):
    if x % 2==0:
        print(x, end=' ')
print()
for x in list:
     if x % 2==0:
         print(x,end=' ')
print('\n\n')

#3. print odd numbers from 5 to 30 and above list
for x in range(5,30):
    if x % 2==1:
        print(x,end=' ')
print()
for x in list:
    if x % 2==1:
        print(x, end=' ')
print('\n\n')

#4. print numbers divisible by 5 from 1 to 30 and above list
for x in range(1,30):
    if x % 5==0:
        print(x, end=' ')
print()
for x in list:
    if x % 5==0:
        print(x, end=' ')
print('\n\n')

#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for x in range(1,100):
    if x % 5==0:
        print(x, end=' ')
print()
for x in range(1,100):
    if x % 7==0:
        print(x, end=' ')
print()
for x in list:
    if x % 5==0:
        print(x, end='')
print()
for x in list:
    if x % 7==0:
        print(x, end='')
print('\n\n')

#6. sum of numbers from 10 to 25 and above list    # not learning
sum=0
for x in range(10,25):
    sum += x
    print('sum of number 10 to 25 is: ', sum )
print('\n\n')

#7. multiplication table of a number    # not lerning
n = int(input('enter the number of multiplication: '))
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')
print()

#8. factorial    #not lerning
n= int(input('enter the number of factorial: '))
product=1
for x in range(1, n + 1):
    product *= x
print(f'factorial of {n} is {product}')

#9. fibonacci          # not lerning
n = int(input('enter number of fibonacci terms:'))
a =0
b =1
for x in range(n):
   print(a, end='')
   a,b = b, a+b
print()
#10. reverse a string
string = input('enter a string')
rev =''
for x in range(len(string)-1,-1,-1):
    rev +=string[x]
print(f'Reverse of {string} is {rev}')

#11. count vowels in a string   #not lerning
s = input()
count = 0
for c in s:
    if c in 'aeiouAEIOU':
        count += 1
print(f'total vowals in the  string is{count}')


#12. count z's and y's in a string   #not lerning
s= input('enter the string to count z\'s and y\'s:')
count =0
for c in s:
    if c in 'zZyY':
        count +=1
print(' total z\'s and y\'s in give string is', count )

#13. check whether a number is prime number or not  # not lerning
n = int(input('enter a number to check prime: '))
if n < 2:
    print('not prime')
else:
    for x in range(2,n):
        if n % x ==0:
            print('not prime')
            break
        else:
            print('prime')
        
            