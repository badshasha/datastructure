# coded by shavendra 'badshasha'

myList = [v for v in range(0,11)]
del myList[4]
print(myList)

def findMissing(list , n):
    sum1 = n * (n+1) / 2
    sum2 = sum(list)

    diff = sum1 - sum2
    if diff > 0:
        print(f'missing number is {diff}')
    else:
        print('no any missing numbers')


findMissing(myList,10)
