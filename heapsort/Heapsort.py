# This script is to perform heap sort on a given list of nummber .
# his is part 3 of 3 in achieving heapsort algorithm

from Build_Max_Heap import build_max_heap
from Max_heapfiy import max_heapify

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr


def heapsort(array):
    array = build_max_heap(array)
    # print(array)
    heap_size = len(array)
    for i in range (len(array)-1,0,-1):
        # print(array)
        array = swap(array,0,i)

        heap_size = heap_size - 1
        array = max_heapify(array,0,heap_size)
    return array
    


A = [16,14,10,8,7,9,3,2,4,1]
answer = heapsort(A)
print(answer)