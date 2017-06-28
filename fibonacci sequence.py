def fibonacci_sequence(limit): # fibonacci sequence generating function
    a =0; b = 1
    while b <= limit:
        print(b); c = a; a = b; b = a + c

# Validates user input before proceeding to find the prime factors
def input_validator(value):
    try:
        int(value)
        return "valid"
    except:
        return "invalid"

N = input("Enter Nth number\n")
if input_validator(N) == "valid":
    if int(N)<0:
        print("Enter positive number")
    else:
        fibonacci_sequence(int(N))
else:
    print("Invalid Integer")