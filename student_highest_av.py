n=int(input())
d={}
k=[]
for i in range(n):
    y=input()
    h=y.split()
    key=h[0]
    val=float(h[1])
    if key in d:
        k.append(key)
        d[key]=(d[key]+val)
    else:
        d[key]=val
y=list(set(k))
for t in y:
    c=k.count(t)
    d[t]=d[t]/(c+1)
print("Total students:",len(d))
t=list(d.values())
p=max(t)
y=t.index(p)
j=list(d.keys())
print('Highest average:',j[y])
for i,v in d.items():
    print(i+':',v)
