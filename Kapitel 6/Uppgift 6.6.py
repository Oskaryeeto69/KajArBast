a = []
räknare = 0
inp = input("Enter number of elements : ") 
for i in range (0, int(inp)):
    a.append([])
    for j in range(0,10):
        a[i].append((i+1)*(j+1))
for tal in a:
    print(a[räknare])
    räknare = räknare + 1