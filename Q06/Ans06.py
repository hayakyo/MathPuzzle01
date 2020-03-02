count = 0

for i in range(2, 10000, 2):
    j = i * 3 + 1
    while True:
        if j == i:
            count += 1
            break
        elif j == 1:
            break
        else:
            if j % 2 == 0:
                j = j / 2
            else:
                j = j * 3 + 1

print(count)
