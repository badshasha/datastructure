
array = [1,2,3]




def loopmethod(array):
    temp = 1
    for value in array:
        temp *= value
    print(temp)

loopmethod(array)


def recursivemethod(array):
    if len(array) == 0:
        return 1
    return array[0] * recursivemethod(array[1:])


v = recursivemethod(array)
print(recursivemethod([1,2,3,10]))
print(v)
