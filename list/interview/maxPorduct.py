

import numpy as np
myArray = np.array([v for v in range(13)])

test2 = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])


# close product
def find_max(myArray):
    temp_product = 0
    pair =""
    for i in range(len(myArray)):
        if i+1 < len(myArray):

            value = myArray[i] * myArray[i+1]
            if temp_product < value:
                temp_product = value
                pair = ""
                pair = f'{myArray[i]} , {myArray[i+1]}'
        else:
            break
    return (temp_product,pair)


print( find_max(test2))


# whole list
# supper bad becaseu O(n)
def find_fromAll(myArray):
    temp_max_product = 0
    pair = ""
    for i in range(len(myArray)):
        for j in range(i+1,len(myArray)):
            value =  myArray[i] * myArray[j]
            if value > temp_max_product:
                temp_max_product = value
                pair = f"{myArray[i]} , {myArray[j]}"
    return (temp_max_product , pair)


print(find_fromAll(test2))
