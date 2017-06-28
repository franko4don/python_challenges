def count_words_in_string(words):
    print("Total number of words in string is %d" %len(str.split(words, ' ')))


def count_words_in_file(filename):
    try:
        print("Total number of words in file is %d" %len(str.split(open(filename, 'r').read(), ' ')))
    except:
        print("Cannot find file")


sentence=input("Enter a sentence\n")
file=open("words.txt", "w")
file.write(sentence)
file.close()
count_words_in_file("words.txt")
count_words_in_string(sentence)
