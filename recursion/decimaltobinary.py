def binary(number):
    assert number >= 0 and int(number) == number , 'the number has to be positive integer'
    if number == 0:
        return 0
    else:
        return number%2 + 10 * binary(int(number/2))

value = binary(256)
print(value)
