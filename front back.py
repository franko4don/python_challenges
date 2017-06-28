def string_division(word):
    divided = []
    temp = list(word)
    if len(word) % 2 == 0:
        divided.append(temp[0:len(word)//2])
        divided.append(temp[len(word)//2:len(word)])
    else:
        divided.append(temp[0:(len(word)//2)+1])
        divided.append(temp[(len(word)//2)+1:len(word)])
    return divided

def front_back(word1, word2):
    a = string_division(word1)
    b = string_division(word2)
    print("".join((a[0]+b[0]+a[1]+b[1])))

first = input("Enter first word\n")
second = input("Enter second word\n")
front_back(first,second)
