s = input()

a = dict()
cntr = 0

for i in range(len(s) - 1):
    sr = s[i:i+2]
    a[sr] = a[sr] + 1 if a.get(sr) else 1

s = input()

t = set()
for i in range(len(s) - 1):

    k = a.get(s[i:i+2])
    if k and s[i:i+2] not in t:
        cntr += k
    t.add(s[i:i+2])

print(cntr)
