# link :https://www.hackerrank.com/challenges/py-if-else/problem.
 if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
        
        
# link :https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(n):
    if year % 400 == 0:
        return("True")
    elif year % 100 == 0:
        return("False")
    elif year % 4 ==0:
        return("True")
    else:
        return("False")
                    
    leap = False
    
    # Write your logic here
    
    return leap


# take n, if n from 1 to 7 print dayname else print invalid day number
#e.g. 1 - Sunday, 2 - Monday, 3 - Tuesday
n = int(input("Enter a number: "))

if n == 1:
    print("Sunday")
elif n == 2:
    print("Monday")
elif n == 3:
    print("Tuesday")
elif n == 4:
    print("Wednesday")
elif n == 5:
    print("Thursday")
elif n == 6:
    print("Friday")
elif n == 7:
    print("Saturday")
else:
    print("invalid day number")
    