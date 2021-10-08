t = float(input("Temp?"))
if t < 18:
    print("Det är kallt")
    print("Sätt på värmen")
    if t < 12:
        print("Sätt på jackan")
        if t < 4:
            print("Det är väldigt kallt")
            if t < -10:
                print("Sätt på värmen, Det är väldigt väldigt kallt")
                if t < -20:
                    print("Det är svinkallt, sätt på värmen eller dra härifrån")
else:
    print("Det är varmt")
    if t >=22:
        print("Stäng av värmen")
        if t >= 30:
            print("Det är svinvarmt, stäng av värmen nu!")
            if t >= 40:
                print("Det är ökenhett, stick härifrån nu!")
            
print(f"Det är {t:.1f} grader")