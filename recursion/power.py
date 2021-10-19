

def power(number):
    i = 0
    power = 1
    while i < number:
        power *= 2
        i += 1
    return power


def recursive(number):
    if number == 0:
        return 1
    else:
        return recursive(number -1 ) * 2
