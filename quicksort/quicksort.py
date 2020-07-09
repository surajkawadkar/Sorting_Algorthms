from Partition import partition
# This sccript is to run quick sort on a list of numbers

def quicksort(array,start,end):
    
    if(start<end):
        # print(array,start,"Hello")
        array,index = partition(array,start,end)
        array = quicksort(array,start,index)
        array = quicksort(array,index + 1,end)
    
    return array

A = [4,6,2,3,1,3]
answer = quicksort(A,0,len(A))
print(answer)