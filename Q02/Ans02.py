operator_names = ['', '+', '-', '*', '/']

for x in range(1000, 10000):
    x_str = str(x)
    for i1 in operator_names:
        for i2 in operator_names:
            for i3 in operator_names:
                cal_str = x_str[0:1] + i1 + x_str[1:2] + i2 + x_str[2:3] + \
                          i3 + x_str[3:4]
                if len(cal_str) == 4:
                    continue
                try:
                    y = eval(cal_str)
                    if x_str[::-1] == str(int(y)):
                        print(x_str, cal_str, y)
                except (NameError, ZeroDivisionError, SyntaxError):
                    continue
