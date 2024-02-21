import sys

m = set()
for line in sys.stdin:
    if line == "\n":
        break
    m.update(line.rstrip().split())

print(len(m))
