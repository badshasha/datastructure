# code by 'badshasha'
memsize = 10;
memory1 = [None for value in range(memsize)]
memory2 = [None for value in range(memsize)]
name = "shavendra"

#
def addValue(array,index,value):
    array[index] = value

# normal search function for mem 1 array
def searchAlgo(array,keyword):
    temp = 0
    for element in array:
        temp += 1
        if element == keyword:
            print("find it ")
            print(temp)
            return
    print("not on the list")


# hash funciton inserting for mem 2 array
def hashFunction(value):
    total = 0
    for i in value:
        total += ord(i)
    position =  total % memsize
    if memory2[position] is  None:
        memory2[position] = value
    else:
        print("value find")




addValue(memory1,4,name)
hashFunction(name)
print(memory1)
print(memory2)

searchAlgo(memory1 , name)
hashFunction(name)











