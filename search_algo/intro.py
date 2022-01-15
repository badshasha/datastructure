from xmlrpc.client import boolean

import numpy as np

data = [value for value in range(10)]
target = 50


#liner search 
def linerSearch(array,target) -> boolean:
    for i,element in enumerate(array):
        if element == target:
            print(f"{element} find in position {i}")
            return True
    return False


# iterative binary search 
def BinarySearch(array,target):
    low = 0  # first element 
    high = len(data) -1 # last element 
    array = np.sort(array)
    temp = 0
    while low <= high:
        temp += 1
        middle_position = (low + high) // 2 
        if target == array[middle_position]:
            print(temp)
            return True
        elif target < array[middle_position]:
            high = middle_position - 1 
        elif target > array[middle_position]:
            low = middle_position + 1
    return False
        


def RecursiveBinary(array,target): # i didnt added sorting functionalities 
    if len(array) == 0 :        
        return False
    else:
        middle_position =  len(array) // 2 
        if target == array[middle_position]:
            return True
        elif target < array[middle_position]:
            return RecursiveBinary(array[0:middle_position-1],target)
        elif target > array[middle_position]:
            return RecursiveBinary(array[middle_position+1:],target)
        

    


linerSearch(data,target)
print(BinarySearch(data,target))
print(RecursiveBinary(data,target))