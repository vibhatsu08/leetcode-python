# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.

def checkPerfectNumber (num) :
    if num == 1 :
        return False
    sum = 1
    i = 2
    while (i*i <= num) :
        if num%i == 0 :
            sum += i + num//i
        i += 1
    return sum == num
print(checkPerfectNumber(num = 1))