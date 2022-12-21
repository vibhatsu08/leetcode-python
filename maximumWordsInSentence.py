# Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

def mostWordsFound (sentences) :
    max = 0
    for sentence in sentences :
        wordsCount = 0
        words = sentence.split(" ")
        wordsCount = len(words)
        
        if max < wordsCount :
            max = wordsCount
    return max
    
        
    
print(mostWordsFound(sentences=["alice and bob love leetcode","i think so too","this is great thanks very much"]))