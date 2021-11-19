import random
rlist = []
for i in range (0,100):
    n = random.randint(0,5)
    rlist.append(n)
if 0 in rlist (0,100):
    rlist.remove(0)
print(rlist)