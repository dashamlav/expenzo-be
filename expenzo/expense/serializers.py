from rest_framework import serializers
from .models import Expense
from expenzo_utils.general_utils import ArrayField


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'category', 'currency', 'description', 'receiptImage', 'transactionType']


class ExpenseFilterSerializer(serializers.Serializer):
    minAmount = serializers.IntegerField(required=False)
    maxAmount = serializers.IntegerField(required=False)
    minDate = serializers.DateField(required=False)
    maxDate = serializers.DateField(required=False)
    categories = ArrayField(required=False)
    transactionTypes = ArrayField(required=False)
    sortBy = serializers.CharField(required=True)

    

        


