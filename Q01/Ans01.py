count = 9

while True:
    count = count + 1

    if str(count) != str(count)[::-1]:
        continue
    if format(count, 'b') != format(count, 'b')[::-1]:
        continue
    if format(count, 'o') != format(count, 'o')[::-1]:
        continue
    print(str(count), format(count, 'b'), format(count, 'o'))
    break
