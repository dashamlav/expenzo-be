
from django.http.response import HttpResponse
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from .models import Expense
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ExpenseSerializer, ExpenseFilterSerializer
from rest_framework.pagination import PageNumberPagination
from expense.utils import get_expense_data_csv
from rest_framework.throttling import UserRateThrottle
from .throttlers import DownloadCsvThrottle


def _get_filter_kwargs(user, filtersQuery):
    serializer = ExpenseFilterSerializer(data=filtersQuery)
    serializer.is_valid()
    filters = serializer.data

    minDate = filters.get('minDate', None)
    maxDate = filters.get('maxDate', None)
    minAmount = filters.get('minAmount', None)
    maxAmount = filters.get('maxAmount', None)
    categories = filters.get('categories', None)
    transactionTypes = filters.get('transactionTypes', None)
    sortBy = filters.get('sortBy', '-date')

    filterKwargs = {}
    filterKwargs['appUser'] = user
    filterKwargs['isActive'] = True

    if minDate and maxDate:
        filterKwargs['date__range'] = (minDate,maxDate)
    if minAmount and maxAmount:
        filterKwargs['amount__range'] = (minAmount,maxAmount)
    if categories:
        filterKwargs['category__in'] = categories
    if transactionTypes:
        filterKwargs['transactionType__in'] = transactionTypes

    return filterKwargs, sortBy


class GetAllExpensesView(ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        filterKwargs, sortBy = _get_filter_kwargs(user=user, filtersQuery=self.request.query_params)

        return self.queryset.filter(**filterKwargs).order_by(sortBy)
    

class CreateExpenseView(CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(appUser=self.request.user)


class UpdateOrDeleteExpenseView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        filter_kwargs = {
            'appUser': self.request.user,
            'id' : self.request.data.get('id', None)
        }
        return get_object_or_404(Expense, **filter_kwargs)

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    #Soft delete expense object
    def perform_destroy(self, instance):
        instance.isActive = False
        instance.save()


class DownloadCsvView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [DownloadCsvThrottle]
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        filterKwargs, sortBy = _get_filter_kwargs(user=user, filtersQuery=self.request.query_params)
        expenses = Expense.objects.filter(**filterKwargs).order_by(sortBy)
        csv_file = get_expense_data_csv(expenses=expenses)
        response = HttpResponse(content=csv_file.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=expenses.csv'
        return response
        