def sum_of_each_degit(number):
    s = str(number)
    arr = list(map(int, s))
    return sum(arr)


a = 1
b = 1

count = 1

while count <= 11:
    c = a + b
    if c % sum_of_each_degit(c) == 0:
        count += 1
        print(c)
    a, b = b, c
