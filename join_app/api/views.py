from join_app.models import Contact, Task, Category
from .serializers import ContactSerializer, TaskSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class ContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class OneContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class OneTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SummaryView(APIView):
    def get(self, request, *args, **kwargs):
        task_count = Task.objects.count()
        in_progress_count = Task.objects.filter(process='IN_PROGRESS').count()
        feedback_count = Task.objects.filter(process='AWAITING_FEEDBACK').count()
        priority_count = Task.objects.filter(priority='URGENT').count()
        upcoming_deadline = Task.objects.filter(due_date__gte=timezone.now().date()).order_by('due_date').first().due_date
        to_dos = Task.objects.filter(process='TO_DO').count()
        done = Task.objects.filter(process='DONE').count()
        
        data = {
            'total_tasks': task_count,
            'in_progress': in_progress_count,
            'awaiting_feedback': feedback_count,
            'urgent': priority_count,
            'upcoming_deadline': upcoming_deadline,
            'to_dos': to_dos,
            'done': done
        }
        
        return Response({"data": data})
