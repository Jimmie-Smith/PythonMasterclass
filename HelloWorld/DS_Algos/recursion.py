
#doll = 50

#def openRussianDoll(doll):
  #  if doll == 1:
   #     print('All dolls have been opened')
   # else:
    #    openRussianDoll(doll - 1)
     #   print(doll)
    
#openRussianDoll(doll)   

def getFactorial(n):
    assert n >=0 and int(n) == n, 'must be a positive integer only!'  # 3. Handle any unintentional cases
    if n in [0,1]: # 2. Get the satisying condition
        return 1
    else:
        return n * getFactorial(n-1) # 1. Get the recursive case
    
print(getFactorial(-1))