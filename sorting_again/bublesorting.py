
def bubble_sorting(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j]> data[j+1]:
                data[j] , data[j+1] = data[j+1] , data[j]
    return data

data = bubble_sorting([2,4,6,1,0])
print(data)