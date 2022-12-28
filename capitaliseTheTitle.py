# Capitalize the Title
# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
# If the length of the word is 1 or 2 letters, change all letters to lowercase.Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

def capitaliseTheTitle (str) :
    words = str.split(" ")
    capitalized_words = []
    for word in words:
        if len(word) <= 2:
            capitalized_words.append(word.lower())
        else:
            capitalized_words.append(word[0].upper() + word[1:].lower())
    capitalized_title = " ".join(capitalized_words)
    return capitalized_title

print(capitaliseTheTitle(str="capiTalIze tHe titLe"))