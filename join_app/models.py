from django.db import models
from django.core.validators import RegexValidator

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
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)