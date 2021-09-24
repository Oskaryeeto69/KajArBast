årspris = int(input("Hur mycket kostar ett årkort? ")) #Frågar priset på ett årskort
biljett = int(input('Hur mycket kostar en biljett? ')) #Frågar hur mycket en biljett kostar
ggr = int(input("Hur ofta går du på gym per år: "))
pris1 = årspris
pris2 = biljett * ggr
if pris1 < pris2:
    print("Det är bättre att köpa ett årskort")
else:
    print("Det är bättre att köpa en biljett")

