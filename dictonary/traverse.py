
# created by shavendra 'badshasha'

myDict = {
"name" : "shavendra",
"age" : 27,
"city" : "matale",
"country" : "srilanka"
}

# first method
def traversDictfirst(dict):
    for key  in dict:  #----------------------> O(n) time complexity
        print(f"{key}:{dict[key]}")  # --------------------> O(1) time complexity , space complexity (because we are not storing any new elements)


# seound method
def traversDict(dict):
    for key , value in dict.items(): #----------------------> O(n)
        # print(f"{key}:{dict[key]}")
        print(key,value)  # --------------------> O(1)


traversDict(myDict)
