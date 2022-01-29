

def merge(array):
    return merge_sorting(array , 0 , len(array)-1) 

def merge_final(array, start_index , middle_index , end_index):

    # find boundaries 
    number_of_left_element = middle_index - start_index +1 
    number_of_right_element = end_index - middle_index

    # create array  
    left_array = [0] * number_of_left_element
    right_array = [0] * number_of_right_element

    for i in range(0,number_of_left_element):
        left_array[i] = array[start_index+i]
    
    for j in range(0,number_of_right_element):
        right_array[j] = array[middle_index + 1+ j]
    
    # check element 
    i = 0 
    j = 0
    k = start_index

    while i < number_of_left_element and j < number_of_right_element:
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i+=1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    
    while i < number_of_left_element:
        array[k] = left_array[i]
        k += 1
        i += 1
    while j < number_of_right_element:
        array[k] = right_array[j]
        k += 1
        j += 1
    return array



def merge_sorting(array , start_index  , end_index):
    
    if start_index < end_index:
        middle_index = ( start_index + end_index) // 2
        merge_sorting(array , start_index , middle_index)
        merge_sorting(array , middle_index+1 , end_index)
        merge_final(array,start_index,middle_index,end_index)
    return array

value = merge([2,1])
print(value)