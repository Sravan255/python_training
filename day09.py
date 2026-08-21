# for loop


# list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
#print elements in list with index based for loop
#skip printing even numbers in list
#skip printing odd numbers in list
#when number 2 comes stop printing  
#when first odd number comes stop printing
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'


l= [4,3,2,5,6]
for x in l:
    print(x)
    for x in range(len(l)):
        print(l)
        
#skip printing even numbers in list
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#skip printing odd numbers in list    
 for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
#when number 2 comes stop printing  
for i in rangea(1 ,5):
    if i % 3==0:
        print(i)
#when first odd number comes stop printing        
for i in rangea(1 ,4):
    if i % 4==0:
        print(i)
        
    