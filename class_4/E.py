n = int(input())
d = dict()

for _ in range(n):
    w, h = map(int, input().split())
    if d.get(w) is None:
        d[w] = h
    elif d[w] < h:
        d[w] = h

print(sum(d.values()))
