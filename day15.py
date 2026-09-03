# functions
def add(a,b):
   return
x = (10+20)
print(x) 

def div(a,b):
    return 
y = 5/5
print(y)

def mul(k,n):
    return 
z=2*2
print(z)



#1. Program to check number is palindrome
def check_num_palindrome(n):
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    if rev == nums:
        return True
    else:
        return False

nums = 1221
n = nums
res = check_num_palindrome(n)
print(res)

#2. Program to check string is palindrome
#method1 (Brute force Approch)
def check_str_palindrome(word):
    rev = ""
    for char in word:
        rev = char + rev 
    if rev == word:
        return True
    else:
        return False


word = "madam"
res = check_str_palindrome(word)
print(res)

# method2 (Optimal)
def check_str_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


word = "madam"
res = check_str_palindrome(word)
print(res)

#3. Program to check prime number
def check_prime_number(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"  
    

n = 13
res = check_prime_number(n)
print(res)


#4. Program to reverse a string
#Using Slicing
def reverse_string(word):
    rev = word[::-1]
    return rev


word = "Akshith"
res = reverse_string(word)
print(res)

#Without using Built-in
def reverse_string(word):
    word = list(word)
    left = 0
    right = len(word) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return ''.join(word)
    



word = "Akshith"
res = reverse_string(word)
print(res)


#5. Program to find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


n = 5
res = factorial(n)
print(res)

#6. Program to find nth fibonacci 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a 
    
    
n = 8
res = fibonacci(n)
print(res)

#6. Program to find fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b 
    print()
    
    
n = 8
fibonacci(n)


#7. Program to count the number of digits
def count_digits(n):
    count = 0
    while n > 0:
        count += 1 
        n //= 10
    return count



n = 12345
res = count_digits(n)
print("Count of digits: ", res)


#8. Program to find Armstrong number
def check_armstrong(n):
    original = n
    #finding count
    count = 0
    while n > 0:
        n //= 10
        count += 1
    
    # finding Armstrong sum
    n = original
    res = 0
    while n > 0:
        digit = n % 10
        power = digit ** count
        res += power
        n //= 10
    return res




nums = 153
n = nums
res = check_armstrong(n)
if res == nums:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")




    