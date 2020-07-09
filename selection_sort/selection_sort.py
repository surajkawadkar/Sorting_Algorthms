#  This script is to perform selection sort on a Array of numbers
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    return arr

def selection_sort(array):
    
    for i in range(0,len(array)):
        smallest = i
        
        for j in range(i+1,len(array)):
            
            if(array[j]<array[smallest]):
                smallest = j
       
        
        array = swap(array,i,smallest)
        
            
                

            
        
        # print(array)
    return array

A =[5,4,3,2,1,90,998]
answer = selection_sort(A)
print(answer)