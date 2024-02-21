n, k = map(int, input().split())

s = input()

v = dict()
m = 1
start, length = 0, 1
l, r = 0, 0
v[s[l]] = v[s[l]] + 1 if v.get(s[l]) else 1

while r < n - 1:
    r += 1
    while max(v.values()) > k:
        v[s[l]] = v[s[l]] - 1
        l += 1

    v[s[r]] = v[s[r]] + 1 if v.get(s[r]) else 1
    if max(v.values()) <= k and r - l + 1 > length:
        start = l
        length = r - l + 1

print(length, start + 1)
