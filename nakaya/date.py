
import datetime
from dateutil import relativedelta

# src : datetime.datetime
def getWeekdayJP(src):
    list_jp = ["月","火","水","木","金","土","日"]
    return list_jp[src.weekday()]


class YearMonth:
    #src : 201806
    def __init__(self, src):
        self._date = src
        self._srcdate = datetime.datetime.now()
        self._initdate = datetime.datetime.now()
        try :
            self._srcdate = datetime.datetime.strptime(self._date, "%Y%m")
        except ValueError as ve:
            print(ve)
            print("set now time:" + self._initdate.strftime('%Y/%m/%d'))

    def daysInMonth(self):
        dst = self._srcdate + relativedelta.relativedelta(months=1)
        return (dst - self._srcdate).days

    def daysListInMonth(self):
        dst = []
        idx = self.daysInMonth()
        dst = [self._srcdate + relativedelta.relativedelta(days=i) for i in range(idx) ]
        return dst

if __name__ == '__main__':
    ym = YearMonth("201806222")
    date_format = lambda x : x.strftime('%Y%m%d') + "(" + getWeekdayJP(x)  +")"
    print(list(map(date_format, ym.daysListInMonth())))