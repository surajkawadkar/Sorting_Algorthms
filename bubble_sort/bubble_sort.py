# This script is to perform bubble sort on a given array of elements

def swap(a,i):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
    return a
    
def bubble_sort(array):
    swap_ctr = -1
    
    while(swap_ctr != 0):
        swap_ctr = 0
        for i in range(0,len(array)-1):
            if(array[i]>array[i+1]):
                array = swap(array,i)
                swap_ctr = swap_ctr + 1
    return array

A = [8,2,45,12,42,3]
print(A)
answer = bubble_sort(A)

print(answer)