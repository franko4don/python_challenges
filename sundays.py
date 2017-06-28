from random import randint
for i in range(200):
    a, b, c = randint(1, 4000), randint(1, 2000), 100000000007
    first = ((a % c) * (b % c)) % c
    second = (a ** b) % c
    print(str(first)+"  "+str(second))
