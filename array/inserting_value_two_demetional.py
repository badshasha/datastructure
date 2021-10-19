# coded by shavendra "badshasha"
# when adding new element of the two dementional array
# whole the column need to move to secound position

# same thing happens for the row
# is the new row applies it's push other rows one step down
# very time consuming operation


import numpy as np

array =np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(array)


new_array = np.insert(array,0,[1,2],axis=1)
print(new_array)
