'''
This is a function that takes a phrase and returns the translation.

'''


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

string=input("Enter a phrase: ")
print(translate(string))