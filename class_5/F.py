n = int(input())

seq = list(map(int, input().split()))
seq.sort()

m = int(input())
prices = []
for _ in range(m):
    power, price = map(int, input().split())
    prices.append([power, price])
prices.sort(key=lambda x: x[1])

seq_it = 0
price_it = 0
total = 0

while seq_it < n:
    while prices[price_it][0] < seq[seq_it]:
        price_it += 1
    total += prices[price_it][1]
    seq_it += 1

print(total)
