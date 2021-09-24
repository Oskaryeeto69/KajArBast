pris = float(input('Hur mycket kostar det per minut när du ringer?')) #Frågar priset per minut när du ringer
minut = int(input('Hur många minuter ringer du per månad?')) #Frågar hur mycket man ringer per månad

totpris = pris * minut

if totpris > 300:
    totpris = totpris * 0.9
else:  
    totpris = totpris

print (f'Det kostar{totpris:.2f} kr')