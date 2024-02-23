n, m = map(int, input().split())

events = []
for i in range(n):
    event = list(map(int, input().split()))
    events.append((min(event), -1))
    events.append((max(event), 1))

points = list(map(int, input().split()))

events.extend([(points[i], 0, i) for i in range(len(points))])
events.sort()

cntr = 0

for i in range(len(events)):
    if events[i][1] == -1:
        cntr += 1
    elif events[i][1] == 1:
        cntr -= 1
    else:
        points[events[i][2]] = cntr

print(*points)
