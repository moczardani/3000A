lista = []

with open("03_000.txt", "r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

print("fajl bezarva, lista beolvasva")

print(f'1. Hany eleme van a sorozatnak? {len(lista)}')


def van_negativ_szam(l):
    for elem in lista:
        if elem < 0:
            return True
    return False

print(f'2. Van-e a sorozatban negativ szam? {"van" if van_negativ_szam(lista) else "nincs"}')


# nem tul pitonikus
i = 0
while (i<len(lista) and lista[i] >= 0):
    i+=1
print('van' if i<len(lista) else 'nincs')


db = 0
for elem in lista:
    if elem%2==0:
        db+=1

print(f'3. Hany paros szam van a listaban {db}')

print(len(list(filter(lambda x:x%2==0, lista))))