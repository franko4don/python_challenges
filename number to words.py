# This code is aimed at converting figures to words up to trillions
# word representation of numbers
one_nineteen = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
levels = ["", "Thousand", "Million", "Billion", "Trillion"]


# The function below splits a given number and groups them in threes
def get_list(number):
    raw = list(number)
    temp = ""
    processed = []
    while len(raw) > 0:
        temp = raw[len(raw)-1]+temp
        if len(temp) % 3 == 0:
            processed.append(temp)
            temp = ""
        raw.pop()
    if len(temp) > 0:
        processed.append(temp)
    processed.reverse()
    return processed


# this function converts the figures to words
def number_to_words(value, level):

    if len(value) < 3:
        value = (3-len(value))*"0" + value
    processed = ""
    first = int(value[0])
    second = int(value[1])
    third = int(value[2])
    abv_nine = int(value[1:])
    if first != 0:
        processed += one_nineteen[first] + " Hundred "
    if second != 0:
        if abv_nine < 20:
            processed += one_nineteen[abv_nine]
        else:
            processed += tens[second]
            if third != 0:
                processed += " "+one_nineteen[third]
    else:
        if third != 0:
            processed += one_nineteen[third]

    if len(processed) > 0:
        processed += " "+levels[level]+" "
    return processed


for x in range(int(input())):
    a = get_list(input())
    length = len(a)
    if (len(a) == 1) and (int(a[0]) == 0):
        print(one_nineteen[0]); continue
    answer = ""
    for i in range(length):
        answer += number_to_words(a[i], length-1-i)
    print(answer)


