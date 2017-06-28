# This module uses fast modular exponentiation (repeating square technique) to compute powers in 0(log n) time
import math

def mod_pow(a, b, c):
    solution = []  # holds the power multiples
    power = bin(b).lstrip('0b')  # converts the power to binary format
    length = len(power)  # gets the length of the string power
    answer = 1
    solution.append(a)
    for x in range(length-1):  # repeated square implementation
        a *= a
        a %= c
        solution.append(a)
    for y in range(0,len(solution)):
        if power[y] == '1':
            answer *= solution[len(solution)-y-1]
            answer %= c
    return answer


def input_validator(a, b, c):
    try:
        int(a)
        int(b)
        int(c)
        return "valid"
    except:
        return "invalid"

# code execution starts here
a = input("Enter base number\n")
b = input("Enter power\n")
c = input("Enter mod\n")

if input_validator(a, b, c) == "valid":
    a = int(a)
    b = int(b)
    c = int(c)
    if a < 1:
        print("Base a must be greater than zero")
    elif b < 0:
        print("power b must be positive")
    else:
        print(mod_pow(a, b, c))
else:
    print("Invalid number/numbers")
#print(pow(a, b, c))
