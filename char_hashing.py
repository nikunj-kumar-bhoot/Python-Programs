s="azyuyyzaaaa"
q=['d','a','y','u']
d={}
for i in s:
    d[i]=d.get(i,0)+1
for i in q:
    print(f"{i}:{d.get(i,0)}")