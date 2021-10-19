import sys
sys.setrecursionlimit(1000)

def fibonacci(number):
    assert number >= 0 and int(number) == number , 'fibonachi number cannot be negative or floating value '
    if number == 0 or number == 1:
        return number
    return  fibonacci(number -1 ) + fibonacci( number -2 )


print(fibonacci(6))
