import math

i = 1
while True:
    result_sqrt = math.sqrt(i)
    result_str = str(result_sqrt)
    arr = [e for e in result_str if e != '.']
    arr = list(map(str, arr))[0:10]
    if len(list(set(arr))) == 10:
        print(i, result_sqrt)
        break
    i += 1

i = 1
while True:
    result_sqrt = math.sqrt(i)
    result_str = str(result_sqrt - math.floor(result_sqrt))
    arr = [e for e in result_str if e != '.']
    arr = list(map(str, arr))[1:11]
    if len(list(set(arr))) == 10:
        print(i, result_sqrt, arr)
        break
    i += 1
