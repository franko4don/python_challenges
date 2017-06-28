def mix_up(a, b):
    a = list(a)
    b = list(b)
    if len(a) > 1 and len(b) > 1:
        first_part = "".join(a[0:2])
        second_part = "".join(b[0:2])
        del(a[0:2]); del(b[0:2])
        answer = second_part+"".join(a)+" "+first_part+"".join(b)
    else:
        answer = "Length of String is less than two"

    return answer

str_a = input("Enter first string a\n")
str_b = input("Enter second string b\n")

print(mix_up(str_a.lower(),str_b.lower()))
