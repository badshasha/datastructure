# code by shavendra "badshasha"
#  device the givne array into two parts 
# take first element form tunsorted array and find it's correct position if sorted array 
# reapeat until unsorted array is element 

def insertion_search(data):
    for i in range(1,len(data)):
        key = data[i]
        j = i -1 
