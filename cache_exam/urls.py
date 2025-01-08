# myproject/urls.py
from django.urls import path
from myapp.views import event_list

urlpatterns = [
    path('events/', event_list),
]