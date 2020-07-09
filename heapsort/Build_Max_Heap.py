from Max_heapfiy import max_heapify

def build_max_heap(array):
    heap_size = len(array)
    for j in range(len(array)/2,-1,-1):# half down  to the first element at index 0
        array = max_heapify(array,j,heap_size)
    return array

# A = [4,1,3,2,16,9,10,14,8,7]
# answer = build_max_heap(A)
# print(answer)