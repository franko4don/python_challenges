import string
import operator
def most_common(word):
    diction = {}
    for char in word:
        diction[char] = word.count(char)
    sorted_dict = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    keys = list(diction.keys())
    keys.sort()

    sorted_dict = dict(sorted_dict)
    limit = 0
    while len(sorted_dict) > 0:
        highest_count = 0
        highest_word = ""
        position = 0
        for x in range(len(keys)):
            if sorted_dict[keys[x]] > highest_count:
                highest_count = sorted_dict[keys[x]]
                highest_word = keys[x]
                position = x
        del sorted_dict[highest_word]
        del keys[position]
        print(highest_word+" %d" % highest_count)
        limit += 1
        if limit > 2:
            break

most_common(input("Enter a string\n"))
