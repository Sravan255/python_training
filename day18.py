# #Random Password Generator
import random, string 
#          = 'abcdefghijklmnopqrstuvwxyzA-Z' + '1234567890' + '!@#$%^&*...'
characters = string.ascii_letters + string.digits + string.punctuation
password = ''
n = int(input('Enter the length of password:  '))
for i in range(n):
    password += random.choice(characters) 
print(password)

#ATM 
import getpass
balance = 0 
print('Set your ATM Pin: ')
p1 = int(getpass.getpass('Enter the 4 digit pin:  '))
if len(str(p1)) != 4:
    print('Please enter only 4 digit pin:')
    exit() 
p2 = int(getpass.getpass('Re-enter the pin:  '))
pin = None 
if p1 == p2:
    pin = p1 
else:
    print('Pins are not matching, please try again')
    exit() 
while True: 
    print('1. Balance Enquiry')
    print('2. Deposit')
    print('3. Withdrawal')
    print('4. Exit') 
    n = int(input('Enter your choice:  '))
    match n:
        case 1:
            p = int(getpass.getpass('Please enter your pin to continue:  '))
            if p != pin:
                print('Your enterned pin is wrong, please try again')
                break
            print(f'Your account balance is {balance}')
        case 2:
            p = int(getpass.getpass('Please enter your pin to continue:  '))
            if p != pin:
                print('Your enterned pin is wrong, please try again')
                break
            amount = int(input('Please enter the amount to deposit:  ')) 
            balance += amount 
            print('Amount deposited successfully')
        case 3:
            p = int(getpass.getpass('Please enter your pin to continue:  '))
            if p != pin:
                print('Your enterned pin is wrong, please try again')
                break
            amount = int(input('Please enter the amount to withdraw:  '))
            if amount > balance:
                print('Insufficient balance') 
            else:
                balance -= amount 
                print(f'Remaining balance: {balance}')
        case 4:
            break
        case _:
            print('Please enter a valid choice')