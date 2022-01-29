# code by shavendra 
# practice session for the interting sorting 


def insert_sorting(data):
    for i in range(i,len(data)):
        current_value = data[i]
        j = i - 1 
        while j >= 0 and current_value < data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = current_value
    return data

