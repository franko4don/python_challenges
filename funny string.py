def funny_string(value):
    m, n = len(value), 0; value1, value2 = list(value), list(value)
    for i in range(1, m):
        if abs(ord(value1[i])-ord(value1[i-1])) == abs(ord(value2[m-i-1])-ord(value2[m-i])):
            n += 1
    return "Funny" if n == m-1 else "Not Funny"
for j in range(int(input())):
    print(funny_string(input()))
