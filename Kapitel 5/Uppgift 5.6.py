#a = input("Skriv ett amerikanskt datum som mm/dd/åå: ")
a = input("Skriv ett svenskt datum som åååå-mm-dd: ")
månad = a[5:7]
dag = a[8:10]
år = a[:4]
s =  månad + "/" + dag + "/" + år[2:5] 
print("Amerikanskt datum:" + s)