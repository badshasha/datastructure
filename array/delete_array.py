# coded by shavendra 'badshasha'

# in deleteing you can delete middle values
# but after deleating it's array should need to refactor it memeoyr location according to the
# free space

# for assume first element deleted all the other element move
# one index forward and cover the free space in the front



# bin o  O(n) suppper bad situation
# best case O(1)
from array import *

array = array('i',[1,2,3,4])
array.remove(2)
print(array)
