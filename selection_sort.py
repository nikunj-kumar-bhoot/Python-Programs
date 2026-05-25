#in selection sort for arranging elements in asc order, we find minimum elememt each time and push it to left end each time and then start next iteration with the subarray starting from the next element of the last inserted index uptil the last index of the principal array
def s_sort(l):
    n=len(l)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if l[j]<l[min_idx]:
                min_idx=j
        if min_idx!=i:
            l[min_idx]+=l[i]
            l[i]=l[min_idx]-l[i]
            l[min_idx]-=l[i]
    return l
