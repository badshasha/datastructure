
# creted by shavendra 'badshasha'


myList = [1,2,3,4]
print(myList[:2])

myList[:2] = ['x','y']
print(myList)


# pop
# delete
# remove


# without element O(1)
# time complexity O(n)
myList = ['a','b']
myList.pop(1)  # it's return deleted element
print(myList)


# delete method
# time complexity O(n)

myList = [1,2,3,4,5]
del myList[1]
print(myList)


# remove method
# time complexity O(n)

myList.remove(4)  # based on values
print(myList)
