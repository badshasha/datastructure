# coded by shavendra 'badshasha'
import time


myList1 = [2,6,3,9,11]
myList2 = [2,6,3,9,11]
number = 9



# my one is bad
    # why " if temp taget in num" ==== o(n)
    # delete also O(n) =========> there for O(n^3)
def my(num,target):
    x = []
    for i in num:
        temp_target = target - i
        if temp_target in num:
            print(temp_target)
            del num[num.index(temp_target)]
            x.append((i,temp_target))
    return x

s = time.time()
print(my(myList1,9))
e = time.time()
p = e -s

print(f'different {e-s} ')



def findingPairs(nums , target):
    array = []
    for temp,i in enumerate(nums):
        for x in nums[temp+1:]:
            if (i + x )== target:
                if (i , x) or (x , i) not in array: # this thing also O(n^3) but array content small number of element
                    array.append((i,x))
    return array

s = time.time()
print(findingPairs(myList2,9))
e = time.time()

print(f'different {e-s} ')

p2 = e -s


# my new one greate 
def findingPairsUPdate(nums , target):
    dictonary = {}
    array = []
    for temp,i in enumerate(nums):
        for x in nums[temp+1:]:
            if (i + x )== target:
                if not(dictonary.get(i) and dictonary.get(x)): # this thing also O(n^3) but array content small number of element
                    array.append((i,x))
                    dictonary[i] = True
                    dictonary[x] = True
    return array

s = time.time()
print(findingPairsUPdate(myList2,9))
e = time.time()

p3 = e -s
print(f'different {e-s} ')

if(p2>p):
    if(p2>p3):
        print("secound algorithm is slow")
    else:
        print("p3 is the slowest")
else:
    if(p>p3):
        print("p is the slowest algorithm")
    else:
        print("p3 is the slowest alongest")


if(p3>p2):
    print("p2 is the fastest")
else:
    print("p3 is the fastest")
