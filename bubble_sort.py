def b_sort(l):
    n=len(l)
    for i in range(n-1):
        is_swap=False
        for j in range(n-1-i):
            if l[j]>l[j+1]:
                is_swap=True
                l[j],l[j+1]=l[j+1],l[j]
        if is_swap==False:
            break
    return l
