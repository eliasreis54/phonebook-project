from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(), name='contact-list'),
]