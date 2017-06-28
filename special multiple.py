def special_multiple(N):
        b = 1
        while (int(bin(b).lstrip('0b')) * 9) % N != 0:
            b += 1
        return int(bin(b).lstrip('0b')) * 9
T = int(input())
for i in range(T):
    print(special_multiple(int(input())))
