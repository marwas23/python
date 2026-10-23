n =10
for i in range(n):
    for j in range(n):
        if i==0 or i==9 or j==0 or j==9:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()