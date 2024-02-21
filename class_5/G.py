n, k = map(int, input().split())

seq = list(map(int, input().split()))

ans = {1: 1, 2: 3, 3: 6}
l, c, r = 0, 1, 2
start = l
total = 0
v = set()
while r < n:
    l = start
    while seq[l] * k < seq[r]:
        l += 1
        c = l + 1
    if c == r:
        r += 1
    if r == n:
        break

    start = l
    while l < r - 1:
        c = l + 1
        while c < r:
            if (seq[l], seq[c], seq[r]) not in v:
                v.add((seq[l], seq[c], seq[r]))
                total += ans[len(set((seq[l], seq[c], seq[r])))]
            c += 1
        l += 1

    r += 1

print(total)
