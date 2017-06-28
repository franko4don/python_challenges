"""
 Program: is_isogram.py
 Author: Ezeoke Onyekachi Samuel
 Description: A method is_isogram that tests a word to know if its Isogram
"""
def is_isogram(self,word):  # removed self
    if type(word) != str:
        # Check if argument is a string
        raise ValueError("Argument should be a string")
    elif len(word) == 0:
        # Check if string is empty and return the appropriate tupple
        return word, False
    else:
        #Check the word and return the appropriate message
        wordToLowerCase = word.lower()
        for char in wordToLowerCase:
            if wordToLowerCase.count(char) > 1:
                return word, False
            else:
                return word, True

print(is_isogram("abcdef","abbcdef"))