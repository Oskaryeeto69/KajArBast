
pris = input ('Skriv priset på varan inkl. moms: ')
pris = float (pris)
exklmoms = pris * 0.8
endastmoms = pris - exklmoms
print (f'priset exkl. moms är {exklmoms:6.2f} och moms i kronor är {endastmoms:6.2f}')



#y = x*x
#print("Talet i kvadrat är", y)