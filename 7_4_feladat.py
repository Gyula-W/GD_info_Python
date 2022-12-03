szam1 = int(input('Adj meg egy számot! '))
if szam1%2 == 1:
    print("A megadott szám páratlan")
if szam1%2 == 0:
    print("A megadott szám páros")


import random
szam2 = random.randint (10, 50)
if szam2%2 == 1:
    szam2+=1
print(szam2)

SZAM3 = 15
print(SZAM3)

szamok = [1,50,60,34,42]
thisstuple = (szam1, szam2, SZAM3)
szamok.extend(thisstuple)
print(szamok)

paros_szamok = [x for x in szamok if x % 2 == 0]
print(paros_szamok)

paratlan_szamok = [x for x in szamok if x % 2 == 1]
print(paratlan_szamok)

print(sorted(szamok))

print(len(szamok))

print(max(szamok))

print(sum(szamok))


