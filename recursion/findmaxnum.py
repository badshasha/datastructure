
def findMaxNum(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    return max( sampleArray[n-1] , findMaxNum(sampleArray , n-1) )
array = [1,2,8,4,5]
findMaxNum(array, len(array))


def findMaxSecount(sampleArray):
    if len(sampleArray) == 1:
        return sampleArray[0]
    return max(sampleArray[0] , findMaxSecount(sampleArray[1:]))


max = findMaxSecount(array)
print(max)
