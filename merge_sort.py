def mergeArrays(l1,l2):
    m=[]
    size1,size2=len(l1),len(l2)
    c1=0
    c2=0
    while c1<size1 and c2<size2:
        if l1[c1]<l2[c2]:
            m.append(l1[c1])
            c1+=1
        else:
            m.append(l2[c2])
            c2+=1
    if c1<size1:
        m+=l1[c1:]
    else:
        m+=l2[c2:]
    return m

def merge_sort(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=merge_sort(l[:mid])
    right=merge_sort(l[mid:])
    return mergeArrays(left,right)
#print(merge_sort([4,1,7,9,2,5,3]))
