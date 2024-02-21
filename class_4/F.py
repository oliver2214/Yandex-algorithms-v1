data = dict()
with open("input.txt", "r") as f:
    for line in f.readlines():
        name, item, count = line.split()
        count = int(count)
        if data.get(name) is None:
            data[name] = dict()

        data[name][item] = data[name][item] + count if data[name].get(item) else count

for name in sorted(data.keys()):
    print(f"{name}:")
    for item in sorted(data[name].keys()):
        print(f"{item} {data[name][item]}")
