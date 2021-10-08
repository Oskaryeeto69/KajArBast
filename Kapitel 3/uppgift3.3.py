a = 45
b = 40
c = 35
d = 30
e = 25
poang =int(input('Hur många poäng fick du på provet?'))

if poang >= a:
    print("Du fick A")
elif poang >= b:
    print("Du fick B")
elif poang >= c:
    print("Du fick C")
elif poang >= d:
    print("Du fick D")
elif poang >= e:
    print("Du fick E")
else:
    print("Du fick F")