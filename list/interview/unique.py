import numpy as np

array  = np.array([v for v in range(10)])

dic = {}

def check_unique(array):
    for i in array:
        if dic.get(i) == None:
            dic[i] = 1
        else:
            print(f'{i} is repeated')
            return False
        return True

print(check_unique(array))
