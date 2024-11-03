r=int(input('no of rows'))
c=int(input('no of cols'))
m1=[]
m2=[]
y=[]
for i in range(r):
    t=[]
    for j in range(c):
        t.append(j)
    m1.append(t)
for i in range(r):
    t=[]
    for j in range(c):
        t.append(j)
    m2.append(t)
for i in range(r):
    t=[]
    for j in range(c):
        t.append(m1[i][j]+m2[i][j])
    y.append(t)
for i in range(r):
    for j in range(c):
        print(y[i][j])
        
                
