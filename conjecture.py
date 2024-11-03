n=int(input())
m=[]
while n>1:
    if n%2==0:
        n/=2
        m.append(n)
    else:
        n=n*3
        n+=1
        m.append(n)
for i in m:
    print(int(i))
print("number of steps",len(m))
