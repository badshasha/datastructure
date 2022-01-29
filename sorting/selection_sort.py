# coded by shavendra 'badshasha'

# -- in case of selectin sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted 

def selected_sorting(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data),1):
            if data[j] < data[min_index]:
                min_index = j
#             if min_index is not i:                        >>>>>>>>>>>>>>>>>>>>>>> # yakoo meka waradi shavendra
#                 data[i] , data[min_index] = data[min_index] , data[i]
        if min_index is not i:                        >>>>>>>>>>>>>>>>>>>>>>> # mehema dapan
            data[i] , data[min_index] = data[min_index] , data[i]
    print(data)
   
        
selected_sorting([1,2,3,9,4,6,5])
