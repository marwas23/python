suma = 0
n = int(input("Podaj n: "))
def Suma(n):
    global suma
    for i in range(n + 1):
        suma += i
    return suma

print(Suma(n))
