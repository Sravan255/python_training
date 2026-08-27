# # # while loop
# # n =6
# # while n >0:
# #     print(n, end='')  # initialisation

n = 5
while n > 0:
     print(n, end= '')
     n-=1
print()

n =10
while n < 20:
     print(n, end='')
     n+=2
print()
    
n=5
while n <=10:
     if n ==7:
         n+=1
         continue
     print(n, end='')
     n+=1
else:
        print('loop susses' ,end='')
print()

n=5
while n <=10:
    if n ==7:
        n+=1
        break
    print(n, end='')
    n+=1
else:
    print('loop susses' ,end='')
print()
# # print 1 to 10 while loop
n =1
while n<=10:
    n+=1
    print(n, end='')
print()
# # print even number from 1 to 10
n=1
while n<=10:
   print(n, end='')
   n+=1
print()
# # print number of divisible by both 5 and 7 from 1 to 500
n=1
while n<=500:
    if n % 5 == 0 and n % 7 == 0:
        print(n, end='')
        n+=1
        print()
        count_digit
        n=int(input('enter the number of count digit:  '))
        count=0
while n > 0:
    n = n // 10
    count+= 1
    print(f'number of digits in the give number is:{count}')
print()
# # reverse  number
n= int(input( 'enter the number reverse:'))
temp = abs(n)
rev =0
while temp > 0:
    last_digit = temp % 10
    rev =rev*10+ last_digit
    temp //= 10
    if n <0:
        rev = -rev
        print(f'reverse of the given number is {rev}')
#  pallindrome
n =int(input('Enter the number pallindrome :'))
temp = abs(n)
rev =0
while temp > 0:
    last_digit = temp % 10
    rev =rev*10+ last_digit
    temp //= 10
    if n <0:
        rev = -rev
        if rev == n:
            print('pallindrome')
        else:
            print(' not pallindrome')
#pallindrome string without slicing, without built in function

# this is a for loop method
s = input('enter the string to check pallindrome: ')
rev =''
for x in range(len(s)-1,-1,-1):
    rev+=s[x]
    if s == rev:
        print('pallindrome')
    else:
        print('not pallindrome')
        
# method 2 = two pointers this a while loop method
s = input('enter the string to check pallindrome: ')
i,j =0,len(s)-1
while i<j:
    if s[i] !=s[j]:
        print(' not a pallindrome')
        break
    i+=1
    j-=1
else:
    print('pallindrome')
# armstrong number
n= int(input('enter a number to check armstrong number:'))
total_digit = len(str(n))
sum =0
temp=n
while temp >0:
    last_digit = temp % 10
    sum+= last_digit ** total_digit
    temp //=10
if n==sum:
    print('armstrong number')
else:
    print('not a armostrong number')
print()
print()

            
    
        
    

        
        
        
    
    
    