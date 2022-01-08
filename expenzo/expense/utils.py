import io
import csv

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