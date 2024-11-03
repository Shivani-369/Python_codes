n=input()
t=list(n)
t.insert(0,'0')
t.append('0')
g=0
for i in range(len(n)):
    if t[i]=='0' and t[i+1]!='1' and t[i+2]!='1':
        t[i+1]='1'
        g+=1
print(g)

        
        
