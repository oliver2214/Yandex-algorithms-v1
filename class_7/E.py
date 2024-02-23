n = int(input())
events = []
in_work = 0
total_mins = 0

for _ in range(n):
    h_start, m_start, h_end, m_end = map(int, input().split())
    if h_end * 60 + m_end == h_start * 60 + m_start:
        in_work += 1
        continue
    events.append((h_start * 60 + m_start, -1))
    events.append((h_end * 60 + m_end, 1, h_start * 60 + m_start))

events.sort()


for i in range(len(events)):
    if events[i][1] == -1:
        in_work += 1
    else:
        if events[i][2] < events[i][0]:
            in_work -= 1

for i in range(len(events)):
    if events[i][1] == -1:
        in_work += 1
    else:
        if in_work == n:
            total_mins = total_mins + events[i][0] - events[i - 1][0] if i > 0 else total_mins + 1440 - events[-1][0] + events[i][0]
        in_work -= 1

if not events:
    total_mins = 1440

print(total_mins)
