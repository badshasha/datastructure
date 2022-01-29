
def selective_sort(data):
    for i in range(len(data)):
        min_index = i 
        for j in range(i+1,len(data)):
            if data[min_index] > data[j]:
                min_index = j
            if i is not min_index:
                data[i] , data[min_index] = data[min_index] , data[i]
    return data

data = selective_sort([1,2,6,4,8,0])
print(data)