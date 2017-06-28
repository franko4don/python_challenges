def pig_latin(word):
    temp = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    addition = ""
    for vowel in vowels:
        if temp[0] == vowel:
            count += 1
    if count >0:
        return "".join(temp)+"way"
    else:
            while count == 0 and len(temp) > 0:
                temp_count = 0
                for vowel in vowels:
                    if vowel == temp[0]:
                        count = 1
                        break
                if count > 0:
                    break
                addition+=temp[0]
                del(temp[0])
    return "".join(temp)+addition+"ay"

words = input("Enter a word\n")
words.replace(" ","")
print(len(words))
if len(words) == 0:
    print("Enter a non empty string")
else:
    print(pig_latin(words))
