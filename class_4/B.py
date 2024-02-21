res = dict()
result = list()
with open("занятие_4/input.txt", "r") as f:
    for word in f.read().split():
        res[word] = res[word] + 1 if res.get(word) is not None else 0
        result.append(res[word])

print(*result)
