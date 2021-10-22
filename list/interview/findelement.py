import numpy as np


list = [v for v in range(1,29)]
myArray = np.array(list)


# linear search algorithum
target = 4
def find_number(myArray,target):
    for element in myArray:
        if target == element:
            print("value find")
        else:
            print("value not found")
