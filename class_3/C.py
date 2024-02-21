n, m = map(int, input().split())

stn = set()
stm = set()
stboth = set()
for _ in range(n):
    stn.add(int(input()))

for _ in range(m):
    num = int(input())
    if num in stn:
        stboth.add(num)
        stn.remove(num)
    else:
        stm.add(num)

print(len(stboth))
print(*sorted(stboth))
print(len(stn))
print(*sorted(stn))
print(len(stm))
print(*sorted(stm))
