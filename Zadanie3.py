def dodaj(a, b):
    return a + b
    
def odejmij(a, b):
    return a - b
    
def pomnoz(a, b):
    return a * b
    
def podziel(a, b):
    return a / b
    
x = float(input("Podaj pierwsza liczbe: "))
y = float(input("Podaj druga liczbe: "))

print("Suma: ", dodaj(x, y))
print("Różnica: ", odejmij(x, y))
print("Mnożenie: ", pomnoz(x, y))
print("Dzielenie: ", podziel(x, y))