# This script is part 1 of 3 in the heap sort algo
# This script will create a max heap given a an aray and an index
# This script will also include some basic funtionality including Left of parent, Right of parent
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def max_heapify(array,index,heap_size):
    l  = left_child(index)
    r  = right_child(index)
    
    if(l<heap_size and array[l]>array[index]):
        largest = l
    else:
        largest = index
    if(r<heap_size and array[r]>array[largest]):
        largest = r
    if(largest != index):
        array = swap(array,index,largest)
        array = max_heapify(array,largest,heap_size)
    return array
        
# A = [16,14,10,8,7,9,3,2,4,1]
# answer = max_heapify(A,2,len(A))
# print(answer)