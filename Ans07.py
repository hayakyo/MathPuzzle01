from datetime import date, timedelta
enddate = date(2020, 7, 24)
startdate = date(1964, 10, 10)


def date_transrate(date_num):
    return int(format(format(date_num, 'b')[::-1]), 2)


for d in range((enddate - startdate).days + 1):
    date = startdate + timedelta(d)
    date_num = int(date.strftime("%Y%m%d"))
    if date_num == date_transrate(date_num):
        print(date_num)
