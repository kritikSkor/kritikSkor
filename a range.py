from datetime import timedelta, date



def daterange(start, end):
    return [start + timedelta(n) for n in range(int((end - start).days))]

daterange(date(2020, 10, 1), date(2020, 10, 5))
>>> [datetime.date(2020, 10, 1),
     datetime.date(2020, 10, 2),
     datetime.date(2020, 10, 3),
     datetime.date(2020, 10, 4)]
