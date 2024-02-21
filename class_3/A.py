nums = map(int, input().split())
d = dict()

for el in nums:
	d[el] = d[el] + 1 if d.get(el) else 1

print(len(d))
