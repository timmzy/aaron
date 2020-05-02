from django.urls import path, include
from .views import view_that_asks_for_money, success_view

urlpatterns = [
    path('', view_that_asks_for_money, name="pay-view"),
    path('success/', success_view, name='success-view'),
]
