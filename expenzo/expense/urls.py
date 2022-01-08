from django.urls import path
from .views import GetAllExpensesView, CreateExpenseView, UpdateOrDeleteExpenseView, DownloadCsvView

urlpatterns = [
    path('get-expenses', GetAllExpensesView.as_view(), name='get-expenses'),
    path('create-expense', CreateExpenseView.as_view(), name='create-expense'),
    path('update-expense', UpdateOrDeleteExpenseView.as_view(), name='update-expense'),
    path('download-csv', DownloadCsvView.as_view(), name='download-csv')
]