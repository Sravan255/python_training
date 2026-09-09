#Compile time errors
a = (3 4 5)    
  print('hi') 
a = [1,2      
deg f1()    

#Run time errors
a = 10 / 0   
print(x)    
5 + 'r'       
int('Rakesh')
d = {1:'a', 2:'b'}
print(d[5]) 
a = [1,2,3]
print(a[5]) 
#others: ModuleNotFound, ImortError, etc

#disrupts the normal flow of execution of program
print('1')  
print('2')
a = 4 / 0  
print('3')  
print('4')

#Exception handling
print('1')    
print('2')   
try:
    a = 4 / 0 
except ZeroDivisionError:
    print("message: Zero Division Error has occured")
print('3')    
print('4')   

#We cannot handle syntax error
try:
    ded f1()      
except SyntaxError:
    print("message: Syntax Error has occured")

# Different errors
try:
    # a = 10 / 0   
    # print(x)    
    # 5 + 'r'     
    # int('Rakesh')
    d = {1:'a', 2:'b'}
    # print(d[5])  
    a = [1,2,3]
    # print(a[5])    
except ZeroDivisionError:
    print('1')
except NameError:
    print('2')
except (TypeError, ValueError, KeyError, IndexError):
    print('3')

#Catching more than once
try:
    a = 10 / 0 
except ZeroDivisionError:
    print('1')
except ZeroDivisionError:
    print('2')
except ZeroDivisionError:
    print('3')

#Catching Parent before Child 
try:
    a = 10 / 0 
except Exception: 
    print('1')
except ZeroDivisionError:
    print('2')

#Else 
try:
    a = 10 / 2 
    print('0')
except ZeroDivisionError:
    print('1')
except Exception:
    print('2')
else:
    print('3')

#Finally
#error
print('0')
try:
    a = 10 / 0  
except ZeroDivisionError:
    print('1')
else:
    print('3')
finally: 
    print('4') 
# no error
try:
    a = 10 / 2
except ZeroDivisionError:
    print('1')
else:
    print('3')
finally: 
    print('4') 


#raise 
try:
    raise ZeroDivisionError 
except ZeroDivisionError:
    print('1') 

#not catching error 
print('0')
try:
    a = 10 / 0 
except NameError:
    print('1')
print('2')
print('3')

#User defined exception 
class RakeshNotFound(Exception):
    pass 
try:
    raise RakeshNotFound 
except RakeshNotFound:
    print('2')

