import random
rlist = [] # Skapar en lista
for i in range (0,100): # Gör en loop som gör denna sak nedanför 100 ggr
    n = random.randint(0,5) # Väljer nummer melllan 0-5
    rlist.append(n) # Lägger till de nummer i listan
    if 0 in rlist: # Om 0 finns i listan så
        rlist.remove(0) # Ta bort 0 från listan
print(rlist)