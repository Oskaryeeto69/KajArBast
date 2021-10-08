meter = int(input('Släpp bollen från: ')) # frågar hur högt upp du släpper bollen ifrån

centimeter = 100 * meter # säger att 100 centimeter är en meter
studs = 0 # säger att studs är på 0

while centimeter > 1: # medans centimeter är över 1 körs loopen
    centimeter = centimeter * 0.7 # gör centimeter * 0.7
    studs = studs + 1 # räknar hur många gånger den studsar 
    print (f'{centimeter:.2f}cm') # printar
print(f'Bollen studsar {studs} gånger') # printar