import random # Importerar random  
rlist = [] # Är en list
for i in range (0,100): # Loopar denna grej nedanför 100 ggr
    n = random.randint(0,1000) # Tar ett random nummer mellan 0-1000
    rlist.append(n) # Lägger random nummret i listan
    rlist.sort() # Sorterar listan i storleksordning
math = sum(rlist)//100 # Är matten i denna uppgift, summan av listan delat i 100
print (f"Minsta talet är {rlist[0]}\nStörsta talet är {rlist[-1]}\nMedelvärdet är {math}")


