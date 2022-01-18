
# sinking sort 
# each par of adjacent item and order them 


def bubble_sorting(data):
    for i in range(len(data)-1):
        for j in range(len(data) -i -1):
            if data[j] > data[j+1]:
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
    return data


data = bubble_sorting([1,2,5,4])
print(data)
