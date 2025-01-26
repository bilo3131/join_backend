from join_app.models import Contact, Task, Category, Subtasks
from .serializers import ContactSerializer, TaskSerializer, CategorySerializer, SubtaskSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

class ContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class OneContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    
class OneTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class SubtasksView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        subtasks = task.subtasks.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)
    
class OneSubtaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Subtasks.objects.all()
    serializer_class = SubtaskSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class OneCategoryView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
class SummaryView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        task_count = Task.objects.count()
        in_progress_count = Task.objects.filter(status='progress').count()
        feedback_count = Task.objects.filter(status='awaiting').count()
        priority_count = Task.objects.filter(priority='urgent').count()
        upcoming_task = Task.objects.filter(priority='urgent', date__gte=timezone.now().date()).order_by('date').first()
        if upcoming_task:
            upcoming_deadline = upcoming_task.date.strftime('%d.%m.%Y')
        else:
            upcoming_deadline = None
        to_dos = Task.objects.filter(status='todo').count()
        done = Task.objects.filter(status='done').count()
        
        data = {
            'total_tasks': task_count,
            'progress': in_progress_count,
            'awaiting': feedback_count,
            'urgent': priority_count,
            'date': upcoming_deadline,
            'todos': to_dos,
            'done': done
        }
        
        return Response({"data": data})