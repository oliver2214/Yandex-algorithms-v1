base = set(input().split())

m = set()
for el in input():
    m.add(el)

cntr = 0
for el in m:
    if el not in base:
        cntr += 1
print(cntr)
