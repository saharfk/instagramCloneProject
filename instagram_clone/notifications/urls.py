from django.urls import path
from notifications.views import ShowNOtifications

urlpatterns = [
    path('', ShowNOtifications, name='show-notifications'),

]
