def partition(data, low_index , high_index):
    i = low_index - 1
    pivot = data[high_index]

    for j in range(low_index , high_index):
        if data[j] < pivot:
            i += 1
            data[j] , data[i] = data[i] , data[j]
    data[i+1] , data[high_index] = data[high_index] , data[i+1]
    return (i+1)


def quickSort(data,low,high):
    if low < high:
        pi = partition(data,low,high)
        quickSort(data, low , pi-1)
        quickSort(data , pi+1 , high)

