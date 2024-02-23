n, m = map(int, input().split())

events = [(-1, 0), (n, 0)]
for i in range(m):
    event_in, event_out = map(int, input().split())
    events.append((event_in, -1))
    events.append((event_out, 1))

events.sort()
vision = 0
cntr = 0

for i in range(1, len(events)):
    if vision == 0:
        cntr = cntr + events[i][0] - events[i-1][0] - 1 if events[i][0] - events[i-1][0] - 1 > 0 else cntr

    if events[i][1] == -1:
        vision += 1
    elif events[i][1] == 1:
        vision -= 1

print(cntr)
