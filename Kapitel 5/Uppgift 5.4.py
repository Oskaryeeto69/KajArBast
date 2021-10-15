s = input("Skriv en text: ")
i = 0
m = 0
for c in s:
    if c == " " or c == "\t":
        m = i
    i = i + 1
if m > 0:
    print(f"Första vita tecken finns på plats nr {m}")
else:
    print("Det fanns inget vitt tecken")