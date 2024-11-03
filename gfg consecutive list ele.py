n=[1,5,5,5,2,2,2,6,7]
m=[]
for i in range(0,len(n)-2):
    if n[i]==n[i+1]==n[i+2]:
        m.append(n[i])
t=list(set(m))
for i in range(0,len(t)):
    if i==len(t)-1:
        print(t[i])
    else:
        print(t[i],end=',')
    
    
