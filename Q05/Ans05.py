import itertools

coinType = [0, 10, 50, 100, 500]
count = 0

for i in itertools.combinations_with_replacement(coinType, r=15):
    if sum(i) == 1000:
        count += 1

print(count)

