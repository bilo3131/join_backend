from join_app.models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer