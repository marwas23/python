n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

if n<=m:
    step = 1
else:
    step = -1

for i in range(n,m+step,step):
    print(i,end=" ")
