from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Contact(models.Model):
    firstname = models.TextField(max_length=30)
    lastname = models.TextField(max_length=30)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    color = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_color = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.category_name
    
    
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    
    PROCESS_CHOICES = [
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('awaiting', 'Awaiting Feedback'),
        ('done', 'Done'),
    ]
    
    title = models.CharField(max_length=100)  # Task-Titel
    description = models.TextField(max_length=1000, null=True, blank=True)  # Task-Beschreibung
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    assignees = models.ManyToManyField('Contact', related_name='tasks')  # Zuordnung der Kontakte
    date = models.DateField(default=date(2099, 12, 31))  # Standard-Zukunftsdatum
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    status = models.CharField(max_length=20, choices=PROCESS_CHOICES, default='todo')
    
    def clean(self):
        super().clean()
        if self.due_date < date.today():
            raise ValidationError("Das Datum darf nicht in der Vergangenheit liegen.")

    def __str__(self):
        return self.title
    
    
class Subtasks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title