from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Contacts
from .serializers import ContactsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class ContactList(viewsets.ViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def list(self, request):
        queryset = Contacts.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        nameRequest = request.data['name']
        emailRequest = request.data['email']
        phoneRequest = request.data['phone']
        model = Contacts.objects.create(name=nameRequest, email=emailRequest, phone=phoneRequest);
        response = ContactsSerializer(model)
        return Response(response.data)

    def retrieve(self, request, pk=None):
        queryset = Contacts.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ContactsSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        nameRequest = request.data['name']
        emailRequest = request.data['email']
        phoneRequest = request.data['phone']
        queryset = Contacts.objects.get(pk=pk)
        queryset.name=nameRequest
        queryset.phone=phoneRequest
        queryset.email=emailRequest
        queryset.save()
        serializer = ContactsSerializer(queryset)
        return Response(serializer.data)    

    def destroy(self, request, pk=None):
        queryset = Contacts.objects.filter(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 