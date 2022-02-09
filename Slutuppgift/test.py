t1 = str(input('Detta program ska visa de bästa spelarna som bär ett specifikt nummer i NHL - Klicka Enter')) # välkomnar dig till miniräknaren
print('Välj mellan vilka nummer du vill se: ') # frågar vilket räknesätt du vill använda eller om du vill avsluta
print('1. 1-25') 
print('2. 26-50') 
print('3. 51-75') 
print('4. 76-99') 
from lista123 import lista1
from lista123fakta import lista2
while True: 

    val = input('Välj mellan vilka nummer du vill se (1 , 2, 3, 4) ')

    if val in('1', '2', '3', '4'): 
       
        if val == '1':
            print (lista1[0:24])
            t2 = input('Vilket nummer vill du veta mer av: ')
            it2 = int(t2)
            spelare = (lista2[it2-1])
            print(spelare)
        elif val == '2':
            print (lista1[25:49])
            t2 = input('Vilket nummer vill du veta mer av: ')
            it2 = int(t2)
            spelare = (lista2[it2-1])
            print(spelare)
        elif val == '3':
            print (lista2[50:74])
            t2 = input('Vilket nummer vill du veta mer av: ')
            it2 = int(t2)
            spelare = (lista2[it2-1])
            print(spelare)
        elif val == '4':
            print (lista1[75:98])
            t2 = input('Vilket nummer vill du veta mer av: ')
            it2 = int(t2)
            spelare = (lista2[it2-1])
            print(spelare)

else:
    print("lmaooo")
    
#t1 = input("Detta program kommer visa det kändsate spelararen baserat på vilket nummer de har\nVilket tröjnummer mellan 1-99 vill du se: ")
#it1 = int(t1)
#from lista123 import lista1
#spelare = (lista1[it1-1])

#print(spelare)