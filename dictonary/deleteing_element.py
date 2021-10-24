
# coded by shavendra 'badshasha'


myDict = {
    "name" : "shavendra",
    "age" : 27,
    "city" : "matale",
    "country" : "srilanka"
}


# pop method
# delete and returning the value

value = myDict.pop("name")  # ---------------->  0(n)
print(value)
print(myDict)


# pop item
# if you put it empty it' randomly picked value and delete it


# clear melthod
# all elemement deleted for dict
myDict.clear()


# del key word
del myDict["age"]  # dont run this code because it's provide an error ["dict is already empty"]

del myDict  # entierly deleted


# space complexity for all algorithm ----------------------> O(1)
