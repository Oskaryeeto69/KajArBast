import csv
t1 = input("Detta program kommer visa det kändsate spelararen baserat på vilket nummer de har\nVilket tröjnummer mellan 1-99 vill du se: ")
with open ("abc.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(t1.join(row))