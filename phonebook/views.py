from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacts
from .serializers import ContactsSerializer

# Create your views here.
class ContactList(viewsets.ViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
