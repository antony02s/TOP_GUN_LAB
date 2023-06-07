# Create a Python program that checks if a given number is prime or not. The user
# should input a number, and the program should print whether it is prime or not.

def prime_number(number):
    for i in range(2,number):
        if number % i == 0:
            return False
        else:
            return True