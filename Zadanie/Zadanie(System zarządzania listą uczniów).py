gebicz


plik = open("uczniowie.txt", "r", encoding="utf-8")
uczniowie = []
for linia in plik:
  uczniowie.append(linia.strip())
plik.close()


while True:
  print("1 Wyświetl listę uczniów")
  print("2 Posortuj listę alfabetycznie")
  print("3Usuń ucznia z listy")
  print("4 Zakończ program")

  wybor = input("Wybierz opcję: ")


  if wybor == "1":
    print("Lista uczniow:")
    i = 1
    for u in uczniowie:
      print(str(i) + ". " + u)
      i = i + 1


  elif wybor == "2":
    uczniowie.sort()
    print("Lista została posortowana!")


  elif wybor == "3":
    print("Lista uczniow:")
    i = 1
    for u in uczniowie:
      print(str(i) + ". " + u)
      i = i + 1

    numer = int(input("Podaj ucznia do usunięcia: "))
    uczniowie.pop(numer - 1)
    print("Uczeń zostal usuniety")

 
  elif wybor == "4":
    print("Koniec programu")
    break

  else:
    print("Bład")