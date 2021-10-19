# coded by shavendra "badshasha"

import numpy as np

array = np.array([[1,2,3],[4,5,6]])
print(array)


def traveral(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])




traveral(array)
