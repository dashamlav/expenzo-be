from django.urls import path
from .views import GetAllExpensesView
from .views import CreateExpenseView
from .views import UpdateOrDeleteExpenseView
from .views import DownloadCsvView
from .views import GetMonthlyExpenseDataView
from .views import GetCategoryDataView

urlpatterns = [
    path('get-expenses', GetAllExpensesView.as_view(), name='get-expenses'),
    path('create-expense', CreateExpenseView.as_view(), name='create-expense'),
    path('update-expense', UpdateOrDeleteExpenseView.as_view(), name='update-expense'),
    path('download-csv', DownloadCsvView.as_view(), name='download-csv'),
    path('get-monthly-data', GetMonthlyExpenseDataView.as_view(), name='monthly-data'),
    path('get-category-data', GetCategoryDataView.as_view(), name='get-category-data')
]