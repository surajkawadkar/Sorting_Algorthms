## Script to perform insertion sort
# def move(arr,i,j): #i ->larger j ->smaller
#     for k in range(j,i+1):
#         arr[k+1]=arr[k]
#     return arr
"""
Notes:
THe above approach where you find the correct place and move everything is quite tedious and more memory and algorithmically more intensive 
So DO IN PLACE COMPARISON and SHIFTING
USE THE HOLE LOGIC  kinda like the tiles puzzle game
"""

def insertion_sort(array):
    print(array)
    for i in range(1,len(array)):
        key = array[i]
        j = i -1
        while(key < arr[j] and j>=0):
            array[j+1] = array[j]
            j = j - 1
            
        array[j+1] = key
    return array
        
        
            
            


print("This script performs insertion sort on a given list of number")

array_size = int(input("Enter the nummber of elements in the array: "))
arr = []
print("Genrating list ./--")
for i in range(0,array_size):
    temp = int(input("Enter the " + str(i) + "th number of the array"))
    arr.append(temp)


answer = insertion_sort(arr)
print(answer)