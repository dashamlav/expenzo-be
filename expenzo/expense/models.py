from django.db import models
from accounts.models import AppUser
from expense import ExpenseCategory, TransactionType
from accounts import CurrencyType
# Create your models here.


class Expense(models.Model):
    appUser = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=50, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=CurrencyType.Choices, null=False, blank=False, default=CurrencyType.INR)
    category = models.CharField(max_length=4, choices=ExpenseCategory.Choices, default=ExpenseCategory.OTHER, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=True)
    receiptImage = models.FileField(upload_to='expense_files', null=True, blank=True)
    transactionType = models.CharField(max_length=4, choices=TransactionType.Choices, null=True, blank=True)
    isActive = models.BooleanField(null=False, blank=False, default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {str(self.date)}'


class Collection(models.Model):
    appUser = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=True)
    expenses = models.ManyToManyField(Expense, related_name='collections', null=True, blank=True)
    isActive = models.BooleanField(null=False, blank=False, default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def totalExpense(self):
        allExpenses = self.expenses.filter(isActive=True).values_list('amount', flat=True)
        return sum(allExpenses)
