def uczen(imie, wiek=18):
    return f"Uczen {imie} ma {wiek} lat."
    
imie_input = input("Podaj imie: ")
wiek_input = input("Podaj wiek: ")

print(uczen(imie_input, wiek_input))

tylko_imie= input("Podaj tylko imie kolejnego ucznia: ")
print(uczen(tylko_imie))