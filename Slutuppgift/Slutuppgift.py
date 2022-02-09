
t1 = input("Detta program kommer visa det kändsate spelararen baserat på vilket nummer de har\nVilket tröjnummer mellan 1-99 vill du se: ")
it1 = int(t1)
from lista123 import lista1
spelare = (lista1[it1-1])

print(spelare)