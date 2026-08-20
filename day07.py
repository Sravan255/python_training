#write the outputs before executing
#TASK 1
n = 9
if n % 3 == 0:
    print('A')
print('Outside')
'''
Write Output: 
A ,Outside

'''

#TASK 2:
n = 10
if n % 10 == 0:
    print('A')
if n % 5 == 0:
    print('B')
print('Outside')
'''
Write Output: 
A, outside
'''


#TASK 3:
n = 10 
if n % 10 == 0:
    print('A')
elif n % 5 == 0:
    print('B')
print('Outside')
'''
Write Output: 
 A,outside
'''

#TASK 4:
n = 10 
if n % 6 == 0:
    print('A')
elif n % 3 == 0:
    print('B')
else:
    print('C')
print('Outside')
'''
Write Output: 
C ,outside
'''

#TASK 5:
marks = 89 
if marks > 40:
    if marks > 75:
        print('Dictinction') 
    else:
        print('Pass')
else:
    print('Fail')
'''
Write Output: 
Dictinction
'''


# x ="hello"
#Y ="world"
#print(x and Y)
