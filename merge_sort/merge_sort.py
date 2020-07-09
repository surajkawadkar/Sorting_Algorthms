from merge import merge
# this script uses the merge functionality defined earlier

def merge_sort(a):
    if(len(a)== 1):
        return a

    a_left = merge_sort(a[:len(a)/2])
    
    a_right = merge_sort(a[len(a)/2:len(a)])
    ans = merge(a_left,a_right)
    return ans

print("This script is to implement merge sort")
A = [12,23,2123,23,4,421,213]

answer = merge_sort(A)
print(answer)