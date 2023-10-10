import math
def Merge(v, p, q, r):
    n_left = q - p + 1
    n_right = r-q
    r = []
    l = []
    for i in range(n_left):
        l.append(v[p + i]) 
    for i in range(n_right):
        r.append(v[q + i + 1]) 

    i = 0
    j = 0
    k = p

    while(i < n_left and j < n_right):
        if(l[i] <=r[j]):
            v[k] = l[i]
            i = i +1
        else:
            v[k] = r[j]
            j = j + 1
        k = k + 1

    while(i < n_left):
        v[k] = l[i]
        i = i + 1
        k = k + 1
    
    while(j < n_right):
        v[k] = r[j]
        j = j + 1
        k = k + 1


def MergeSort(v,left, right):
    if(left<right):
        mid = math.floor((left+right)/2)
        MergeSort(v,left,mid)
        MergeSort(v,mid+1,right)
        Merge(v, left,mid,right)

v = [5,2,3,4,8,7,100,82,7]

MergeSort(v,0,len(v)-1)
print(v)