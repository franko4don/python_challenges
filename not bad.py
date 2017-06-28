def find(word, sub):
    try:
        return word.index(sub)
    except:
        return -1;


def not_bad(sentence):
    not_pos = find(sentence,"not")
    bad_pos = find(sentence,"bad")
    if not_pos == -1 or bad_pos == -1:
        print(sentence)
    else:
        if not_pos < bad_pos:
            temp = list(sentence)
            print("".join(temp[0:not_pos])+"good")
        else:
            print(sentence)
value = input("Enter a sentence\n")
not_bad(value.lower())