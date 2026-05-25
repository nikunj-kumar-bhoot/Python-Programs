def i_sort(l):
    n=len(l)
    for i in range(1,n):
        if (l[i]<l[i-1]):
            key=l[i]
            j=i-1
            while j>=0 and l[j]>key:
                l[j+1]=l[j]
                j-=1
            l[j+1]=key
    return l