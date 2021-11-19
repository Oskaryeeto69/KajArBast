s = input("Skriv in ett antal heltal")
lista = s.split()
s1 = 0
for t in lista:
    if int(t) <= 0:
        s1 = s1 + 1

print(s1)