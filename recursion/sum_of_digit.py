


def sumOfProduct(number):
    assert number >= 0 and int(number) == number, '[-] number must be positive integer '
    if number == 0:
        return 0
    return number + sumOfProduct(number-1)


number = 3
answer =sumOfProduct(number)
print(f' [+] sumofnumber {number} =  {answer}')
