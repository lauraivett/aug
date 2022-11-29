wr = open('H:\prog\Aug.txt', 'w')
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

havi = False
if len(aug)==31:
    havi = True
    print("Igen")
    wr.write(f"Igen\n")
else:
    print("Nem")
    wr.write(f"Nem\n")

minElem = aug[0]
maxElem = aug[0]
for elem in aug:
    if elem>maxElem:
        maxElem=elem
    if elem<minElem:
        minElem=elem

kern = maxElem
kerm = minElem
i = 0
while aug[i] !=kern:
    i = i +1
y=0
while aug[y] !=kern:
    y = y +1

print(f'A legnagyobb hőmérséklet {maxElem} fok volt')
print(f'A legkisebb hőmérséklet {minElem} fok volt')
wr.write(f'A legnagyobb hőmérséklet {maxElem} fok volt\n')
wr.write(f'A legkisebb hőmérséklet {minElem} fok volt\n')

a = 0
for i in aug:
    if i>31:
        a = a+1
print(f"{a} alkalommal volt a hőmérséklet 31 fok felett")
wr.write(f"{a} alkalommal volt a hőmérséklet 31 fok felett\n")

aug[20]
print(f"A hőmérséklet {aug[20+1]} fok volt augusztus 20.-án.")
wr.write(f"A hőmérséklet {aug[21]} fok volt augusztus 20.-án.\n")

osszeg = 0
for num in aug:
    osszeg = osszeg+num
    
atlag = osszeg/len(aug)
print(f"Átlag: {atlag}")
wr.write(f"Átlag: {atlag}\n")