from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from phonebook import views

router = DefaultRouter()
router.register(r'contacts/$', views.ContactList)
urlpatterns = [
    path('', include(router.urls)),
]