from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name = "mylist"),
    path('delete/', views.delete_item, name='delete_item'),
]