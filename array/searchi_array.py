# created by shavendra "badshasha"

# in werse case array go thought the all the element there for each O(n)
from array import *

myArray = array('i',[1,2,3,4,5])


def search_simple(array,element):
    for value in array:
        if element == value:
            print("find it")
            return
    print("oops looks like values is not on the list")
