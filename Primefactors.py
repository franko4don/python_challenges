# This module  requests for input from user and then generates all the prime factors
# It uses sieve of Eratosthenes to generate prime numbers and also does primality test on a given number if necessary
import math


# This function is used to validate a prime number
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    count = 0
    upper_bound = int(math.sqrt(n)) + 1
    for x in range(3, upper_bound,2):
        if n % x == 0:
            count += 1
            break
    if count > 0:
        return False
    else:
        return True


# Extracts the prime factors of a given number if any
def prime_factors(number):
    for x in range(2,number+1):
        if number % x == 0:
            if is_prime(x):
                print(x)


# Validates user input before proceeding to find the prime factors
def input_validator(value):
    try:
        int(value)
        return "valid"
    except:
        return "invalid"


# code execution starts here
number = input("Enter an integer to calculate prime factors\n")
isvalid = input_validator(number)
if isvalid == "valid":
    number = int(number)
    if number < 0:
        print("Integer must be positive")
    elif number == 0 or number == 1:
        print("No prime factors")
    else:
        prime_factors(number)
else:
    print("Please Enter a valid integer")
