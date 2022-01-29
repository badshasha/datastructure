


from math import ceil, sqrt
import numpy as np

def insert_sorting(data):
    for i in range(1,len(data)):
        current_value = data[i]
        j = i - 1 
        while j >= 0 and current_value < data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = current_value
    return data




def bucket_sorting(data):
    max_value = max(data)
    bucket_number = round(sqrt(len(data)))
    array = [[] for _ in range(bucket_number)]  

    for i in range(len(data)):
        selecte_bucket =   ceil ( (data[i] * bucket_number) / max_value )
        array[selecte_bucket-1].append(data[i])    

    value = []
    for small_array in array:        
        value.append(insert_sorting(small_array))
    
    return [val for array in value for val in array]

print(bucket_sorting([1,3,2,4,8,5,6,11,10]))