
# codded by shavendra 'badshasha'

myDict = {
"name" : "shavendra",
"age" : 27,
"city" : "matale",
"country" : "srilanka"
}


def searchDict(dict , search):
    if search not in dict:
        print("value not found")
    else:
        print(f"value found , {dict[search]}")


searchDict(myDict, "name")
