
# this script figures out where exactly does the pivot element lie in the list of numbers to be sorted
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr

def partition(array,start,end):
    pivot = array[end - 1]
    i = start - 1
    for j in range(start,end):
        if array[j]<pivot:
            i = i + 1
            array = swap(array,i,j)
    array = swap(array,i+1,end -1)
    return array,i+1

# A =[234, 900, 23, 323]
# answer,index = partition(A,0,len(A))
# print(answer,index)