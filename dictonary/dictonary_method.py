

# coded by shavendra "badshasha"


myDict = {
"name" : "shavendra",
"age" : 27,
"city" : "matale",
"country" : "srilanka"
}


# clear dict
myDict.clear()

# copy [ return shallow copy ]
new_dict_copy = myDict.copy()

# fromkeys method --> ( para - 1 ) --> key , ( para - 2) --> value
new_dict = {}.fromkeys([1,2,4],0) # all have same values

# this funciton provide value if not it's provide None vlaue (very userfull method)
null_value = myDict.get("name")

# or we can user it like
hello_value = myDict.get( "name", "badshasha")  # if value not exist on the dict it's return "name"
