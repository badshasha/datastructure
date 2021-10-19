

def someOfDigits(n):
    assert n>-= and int(n) == n , 'the number has to be posittive integer only'
    if n == 0: # cannot devide any more
        return 0
    return int(n%10) + someOfDigits(int(n/10))


print(someOfDigits(112))
