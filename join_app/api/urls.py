from django.urls import path
from .views import ContactsView, OneContactView, TasksView, OneTaskView, CategoryView, SummaryView

urlpatterns = [
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', OneContactView.as_view()),
    path('tasks/', TasksView.as_view()),
    path('tasks/<int:pk>/', OneTaskView.as_view()),
    path('category/', CategoryView.as_view()),
    path('summary/', SummaryView.as_view(), name='task_summary_api')
]
