data = list()
with open("input.txt", "r") as f:
    data = f.read().split()

cur = data[0]
res = {data[0]: 1}

for word in data[1:]:
    res[word] = res[word] + 1 if res.get(word) else 1
    if res[word] == res[cur]:
        cur = min(cur, word)
    elif res[word] > res[cur]:
        cur = word

print(cur)
