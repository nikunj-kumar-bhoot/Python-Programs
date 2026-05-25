n=[5,3,2,2,1,5,5,7,5,10] #1<=n[i]<=10 for all i
m=[10,111,1,9,5,67,2]
hash_list=[]
for i in range(11):
    hash_list.append(0)
for i in n:
    hash_list[i]+=1
for i in m:
    if i>=1 and i<=10:
        print(f"{i}:{hash_list[i]}")