# created by shavendera 'badshasha'


# time complexity O(1)
# space complexity O(1)

myList = [1,2,3,4,5]
print(myList) # print same as the defined section
myList[2] = 33
print(myList)


# inserting element to the

# time complexity O(n)
# move each element one step write

myList = [1,2,3,4,5,5]
myList.insert(0,23)
print(myList)


# append is O(1)

myList.append(1)


# time complexity O(n)
newList = [1,2,3,4]
myList.extend(newList)
