from rest_framework import serializers
from auth_app.models import UserProfile

class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']