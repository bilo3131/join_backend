from django.urls import path
from .views import ContactsView, OneContactView, TasksView

urlpatterns = [
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', OneContactView.as_view()),
    path('tasks/', TasksView.as_view())
]
