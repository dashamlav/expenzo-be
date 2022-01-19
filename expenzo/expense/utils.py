import io
import csv
import datetime
from dateutil.relativedelta import relativedelta
from expenzo_utils.general_utils import aggregateToDict
from expenzo_utils.dateutils import getStartToEndDateRangeForMonth
from .models import Expense
from functools import reduce, partial
from django.db.models import Sum
import itertools

def get_expense_data_csv(expenses):
    csv_file = io.StringIO()
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['TITLE', 'AMOUNT', 'DATE', 'CATEGORY', 'PAYMENT MODE', 'DESCRIPTION'])
    for expense in expenses:
        csv_writer.writerow([
            expense.title, 
            expense.amount, 
            expense.date, 
            expense.get_category_display(), 
            expense.get_transactionType_display(), 
            expense.description,
        ])
    return csv_file

def fetchDataDict(controllerFunc, appUserId, years):

    dataMap = aggregateToDict(
        map(
            lambda yearToMonthDataIt:
                reduce(
                    lambda initial, value: initial.setdefault(value[0], {}).update(value[1]) or initial,
                    yearToMonthDataIt,
                    {}
                ),
            map(
                partial(itertools.starmap, controllerFunc),
                map(
                    partial(zip, itertools.repeat(appUserId), range(1,13)),
                    map(itertools.repeat, years)
                )
            )
        )
    )
    return dataMap

def getMonthlyExpenseData(appUserId, month, year):
    dateRange = getStartToEndDateRangeForMonth(year, month)
    monthName = datetime.datetime.strptime(str(month), "%m").strftime("%b")
    monthTotal = Expense.objects.filter(appUser_id=appUserId, date__range=dateRange).aggregate(Sum('amount'))['amount__sum']
    monthTotal = monthTotal if monthTotal else 0
    return (year,{monthName:monthTotal})

def getFieldWiseMonthlyExpenseData(appUserId, month, year, fieldType=None):
    dateRange = getStartToEndDateRangeForMonth(year, month)
    fieldData = Expense.objects.filter(appUser_id=appUserId, date__range=dateRange).values(fieldType).annotate(Sum('amount'))
    monthName = datetime.datetime.strptime(str(month), "%m").strftime("%b")

    fieldToAmountMap = {}
    for fieldDict in fieldData:
        fieldToAmountMap[fieldDict[fieldType]] = fieldDict['amount__sum']

    return (year,{monthName:fieldToAmountMap})

def getFieldWiseYearlyExpenseData(appUserId, year, fieldType=None):
    daterange = (datetime.date(year,1,1), datetime.date(year,12,31))
    fieldData = Expense.objects.filter(appUser_id=appUserId, date__range=daterange).values(fieldType).annotate(Sum('amount'))
    fieldToAmountMap = {}
    for fieldDict in fieldData:
        fieldToAmountMap[fieldDict[fieldType]] = fieldDict['amount__sum']
    return fieldToAmountMap

