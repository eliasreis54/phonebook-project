from django.shortcuts import render
from rest_framework import generics
from .models import Contacts
from .serializers import ContactsSerializer

# Create your views here.
class ContactList(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
