k = int(input())
ans = []
for _ in range(k):
    n, *time = map(int, input().split())

    events = [None] * (n * 2)
    for i in range(0, n * 2, 2):
        events[i] = ((time[i], -1, i // 2))
        events[i+1] = ((time[i + 1], 1, i // 2))

    cur = 0
    events.sort()
    pool = set(range(n))
    last = -1

    if events[0][0] != 0:
        ans.append("Wrong Answer")
        continue

    for i in range(len(events)):
        if events[i][1] == -1:
            cur += 1
            if cur == 1:
                pool.discard(i)
        else:
            if cur == 1:
                pool.discard(i)
            cur -= 1
        cur -= events[i][1]
        if i != 0:
            if cur == 0 and events[i][0] != 10000:
                ans.append("Wrong Answer")
                break

        if events[i][0] - events[last][0] == 0 and events[i][1] == events[last][1]:
            pool.add(events[last][0])
            pool.add(events[i][0])

        last = i
    else:
        if len(pool) == 0:
            ans.append("Accepted")
        else:
            ans.append("Wrong Answer")

for el in ans:
    print(el)
