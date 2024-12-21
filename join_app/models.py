from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Contact(models.Model):
    firstname = models.TextField(max_length=30)
    lastname = models.TextField(max_length=30)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('URGENT', 'Urgent'),
    ]
    
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ManyToManyField(Contact, related_name='task')
    due_date = models.DateField(default=timezone.now)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='LOW')
    
    def clean(self):
        super().clean()
        if self.due_date < timezone.now().date():
            raise ValidationError("Das Datum darf nicht in der Vergangenheit liegen.")
    
    def __str__(self):
        return self.title
    
class Subtasks(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    competed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title