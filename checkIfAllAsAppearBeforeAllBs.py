# Check if All A's Appears Before All B's
# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

def checkString (s) :
    for i in range (len(s)) :
        if s[i] == "b" :
            if "a" in s[i::] :
                return False
    return True
print(checkString(s="bbb"))