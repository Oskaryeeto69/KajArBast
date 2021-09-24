svar = input('antal sekunder')
sek = int(svar)
print('inmatningen:', sek)
tim = sek // 3600
sek = sek % 3600
print('Rest från timmar:', sek)
min = sek // 60 #delar antalet sekunder på en minut
sek = sek % 60 #använder modulo för att räkna ut antalet sekunder som blev över från minut
print('Rest från minuter:', sek)
print('timmar:', tim)
print('minuter,', min)
print('sekunder,', sek)