# '''
# How to find the sum of digits of an integer using recursion
# '''

def getSumDigits(n):
    assert n >= 0 and int(n) == n, f"{n} is not a positive integer" # cover any unintended cases. In this case we check for negative numbers
    if n == 0: # then we get the base condition
        return 0
    else:
        return int(n % 10) + getSumDigits(int(n/10)) # This is the recursive case. think about the logic of how this works.
    
print(getSumDigits(1594))
