# right angle triangle
n =int(input('enter a number:'))
for i in range(1,n+1):
    print(i * '*')
print()
# inverted right angle triangle
for i in range(n,0,-1):
    print(i *'*')
print()
#pyramid star 
for i in range(1,n+1):
    print((n-i)*' '+i*'* ')
print()
#inverted pyramid 
for i in range(n,0,-1):
    print((n-i)*' ' + i *'* ')
print()
#hollo sqara
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
#star zero based indexing
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i == j or j== n-i-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
#number right angle
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
# row number pattern
for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
print()
# reverse patter number
for i in range(1, n+1):
    for j in range(i, 0 ,-1):
        print(j, end =' ')
    print()
#number pyramid
for i in range(1,n+1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
    # reverse number system
for i in range(n,0,-1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
    # #floyd's
    # for i in range(1,n+1):
    #     for j in range(i):
    #         print(c, end=' ')
    #         c+=1
    #pascal's tringle
    # for i in range(n):
    #     num=1
    #     for j in range(i+1):
    #         print(num, end=' ')
    #         num = num * (i-j) // (j+1)
    #     print()