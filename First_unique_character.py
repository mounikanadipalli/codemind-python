n = input()
x = 0
for i in range(0,len(n)):
    c=n.count(n[i])
    if c==1:
        print(n[i])
        x=1
        break
if x==0:
    print("-1")
