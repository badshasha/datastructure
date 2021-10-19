# coded by shavendra "badshasha"


# big o    O(1) constant time operation 
from array import *

int_array = array('i',[1,2,3,4,5])


def accessElement(array,index):
    if len(array) < index:
        print("entered index lager than the array element count")
        return
    print(array[index])

accessElement(int_array,2)
