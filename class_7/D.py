n = int(input())
events = []

for i in range(n):
    s, e = map(int, input().split())
    if e - s < 5:
        continue
    events.append((s, -1, i))
    events.append((e - 5, 1, i))
events.sort()

max_listeners = set()
listeners = set()
time_1 = 1
sec_max_listeners = set()

for i in range(len(events)):
    if events[i][1] == -1:
        listeners.add(events[i][2])
        if len(max_listeners) < len(listeners):
            max_listeners = listeners.copy()
            time_1 = events[i][0]
    else:
        if len(max_listeners) < len(listeners):
            max_listeners = listeners.copy()
            time_1 = events[i][0]
        listeners.discard(events[i][2])

time_2 = time_1 + 5

for i in range(len(events)):
    if events[i][2] not in max_listeners:
        if events[i][1] == -1:
            listeners.add(events[i][2])
            if len(sec_max_listeners) < len(listeners) and abs(events[i][0] - time_1) >= 5:
                sec_max_listeners = listeners.copy()
                time_2 = events[i][0]
        else:
            if len(sec_max_listeners) < len(listeners) and abs(events[i][0] - time_1) >= 5:
                sec_max_listeners = listeners.copy()
                time_2 = events[i][0]
            listeners.discard(events[i][2])

print(len(max_listeners) + len(sec_max_listeners), min(time_1, time_2), max(time_1, time_2))
