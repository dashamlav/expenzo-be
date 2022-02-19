from django.urls import path
from .views import LoginView, RegisterView, ValidateTokenView, RegisterPreflightView, RefreshAuthTokenView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('register-preflight', RegisterPreflightView.as_view(), name='register-preflight'),
    path('validate-token', ValidateTokenView.as_view(), name='validate-token'),
    path('refresh-token', RefreshAuthTokenView.as_view(), name='refresh-token')
]