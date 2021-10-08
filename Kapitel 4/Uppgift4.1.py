print ('[', end='')
k = 0
while k < 6:
    print (f'{k:2}', end='')
    k = k + 2 # Om man tar den till samma rad som while blir det en loop som spammar 1
    print (']') 