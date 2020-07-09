## This script is to merge two sorted lists
def merge(a,b):
    
    c = []
    if(len(a) == 0):
        return b
    if(len(b) == 0):
        return a
    i = 0
    j = 0
    # k = 0
    while( i != len(a) and  j != len(b)):
        if(a[i]<b[j]):
            c.append(a[i])
            i = i + 1
            # k = k + 1
        else:
            c.append(b[j])
            j = j + 1
            # k = k + 1
    # check if list is finished
    
    if(i == len(a) and j != len(b)):
        # print("Im here 2")
        for elt in b[j:]:
            c.append(elt)
        return c
    if(j == len(b) and i != len(a)):
        # print("Im here 3")
        for elt in a[i:]:
            c.append(elt)
        return c
# print("This script is to perform merge on two sorted Lists")
# A = [13]
# B = [14,21]
# print(len(A),len(B))
# C = merge(A,B)
# print(C)    