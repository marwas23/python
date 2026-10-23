n = int(input("Podaj n: "))
suma = 0
for i in range(n+1):
    suma += i
    print(suma,":",i)
print("Suma n kolejnych wyrazów = ",suma)