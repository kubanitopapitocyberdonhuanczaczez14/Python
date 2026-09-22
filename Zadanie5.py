def produkt(nazwa, cena, sztuki):
    return cena * sztuki
    
nazwa_prod = input("Nazwa: ")
cena_prod = float(input("Cena: "))
ilosc int(input("Sztuki: "))

wynik = produkt(nazwa=nazwa_prod, cena=cena_prod, sztuki=ilosc)

print("Wartość:", wynik)