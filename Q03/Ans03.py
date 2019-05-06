card_array = [False] * 100

for num in range(2, 101):
    for i in range(num-1, 100, num):
        if card_array[i]:
            card_array[i] = False
        else:
            card_array[i] = True

for j in range(0, 100):
    if not card_array[j]:
        print(j+1, end=",")
