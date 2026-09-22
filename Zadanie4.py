def cena_biletu(wiek, cena_podstawowa=30):
    if wiek < 12:
        return 15
    elif wiek <= 17:
        return 20
    else:
        return cena_podstawowa
        
        
wiek_osoby = int(input("Podaj wiek: "))
koszt = cena_biletu(wiek_osoby)
print(f"Cena biletu wynosi: {koszt} zł")