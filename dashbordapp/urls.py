# dashboard/urls.py
from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]