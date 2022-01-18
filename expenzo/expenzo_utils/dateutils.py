
import datetime
from dateutil.relativedelta import relativedelta


def getStartToEndDateRangeForMonth(year, month):
    firstDayOfMonth = datetime.date(year, month, 1)
    lastDayOfMonth = firstDayOfMonth + relativedelta(months=1, days=-1)
    return (firstDayOfMonth, lastDayOfMonth)