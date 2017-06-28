import string
import math
import cmath
alpha = list(string.ascii_lowercase)
number = []
value = input()
ans1 = 0;
ans2 = 0;
mod = 1000000007;
for i in range(len(alpha)):
    count = 0;
    for j in range(len(value)):
        if alpha[i] == value[j]:
            count += 1
    if count > 1:
         number.append(count)

for x in range(len(number)):
    if number[x] >= 4:
        ans1 += math.factorial(number[x])//(math.factorial(4) * math.factorial(number[x]-4))
        ans1 %= mod
for y in range(len(number)):
    if number[x] == 3:
        ans2 += 2;
        ans2 %= mod
print(ans1+ans2);