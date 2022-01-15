import numpy as np 

array = [1,2,3,4,5,6,6,8,9]


def find(array,target):  # my one not good code 
    finding = []
    low = 0
    high = len(array)
    sorted_array = np.sort(array)
    different = None
    while low <= high:        
        middle_value = (low + high) // 2 
        if target == sorted_array[middle_value]:
            print(f"{target} is the value")
        elif target < sorted_array[middle_value]:
            temp_different =sorted_array[middle_value] - target
            if different is None:
                different = temp_different 
                finding.append(sorted_array[middle_value])
            else:
                if different > temp_different:
                    finding.pop()
                    finding.append(sorted_array[middle_value])
                else:
                    print(finding)
                    break
            high = middle_value -1

        elif target > sorted_array[middle_value]:
            temp_different = target - sorted_array[middle_value]
            if different is None:
                different = temp_different 
                finding.append(sorted_array[middle_value])
            else:
                if different > temp_different:
                    finding.pop()
                    finding.append(sorted_array[middle_value])
                else:
                    print(finding)
                    break
            low = middle_value + 1 
         
    print(finding.pop())


def find_closest_number(data , target):
    min_different = None 
    low = 0
    high = len(data) - 1 
    closest_number = None 

    #Edges controll for empty list 
    # list with one elemet 
    if len(data) == 0:
        return None 
    if len(data) == 1:
        return data[0]
    
    while low <= high:
        mid = (low + high) // 2 
        if mid + 1 < len(data):
            min_different_right = abs(data[mid+1] - target)
        if mid > 0:
            min_different_left =  abs(data[mid-1] - target)
        
        if min_different_right < min_different:
            min_different = min_different_right
            closest_number =  data[mid + 1]
        if min_different_left < min_different:
            min_different = min_different_left
            closest_number = data[mid - 1]
        
        # move the mid point accordingly as is done 
        if data[mid] < target:
            low = mid + 1 
        elif data[mid] > target:
            high = mid -1 
        else: # element is the target closest number is it 
            return data[mid]

    return closest_number


find(array,7)


        