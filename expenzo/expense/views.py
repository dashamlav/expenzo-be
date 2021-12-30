
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from .models import Expense
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class GetAllExpensesView(ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(appUser=user, isActive=True).order_by('-date')
    

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


    