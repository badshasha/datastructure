import sys
sys.setrecursionlimit(10000)   # overrite recurcive limit

def factorial(number):
    assert number >= 0 and int(number) == number , 'number must be positive interger'
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number -1)


value = factorial(-4)
print(f"values is {value}")
