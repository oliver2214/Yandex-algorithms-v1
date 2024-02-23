n, d = map(int, input().split())

seq = list(map(int, input().split()))

events = []
c = seq.copy()

for i in range(n):
    events.append([seq[i], i])

events.sort()
seq[events[0][1]] = 1

cntr = 1
ans = 1
tcks = {1: 0}

for i in range(1, n):
    t = 1
    while t <= ans and events[i][0] - events[tcks[t]][0] <= d:
        t += 1

    if t <= ans and events[i][0] - events[tcks[t]][0] > d:
        cntr = t
    else:
        cntr = t
        ans = max(ans, cntr)

    tcks[t] = i
    seq[events[i][1]] = cntr

print(ans)
print(*seq)
