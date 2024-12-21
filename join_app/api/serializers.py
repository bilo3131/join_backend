from rest_framework import serializers
from join_app.models import Contact, Task, Category

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"