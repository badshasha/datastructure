

def arraysum(array):
    if len(array) == 1:
        return array[0]
    return array[0] + arraysum(array[1:])



def reversString(string):
    if len(string) == 1:
        return string[0]
    return string[len(string)-1] + reversString(string[:len(string)-1])


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)


# array = [1,2,3,4]
# print(arraysum(array))
print(reversString("shavendra"))
print(factorial(3))


def power(base,other):
    if other == 0:
        return 1
    if other == 1
        return base
    return base * power(base,other-1)
