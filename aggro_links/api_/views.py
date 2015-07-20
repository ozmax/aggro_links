from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api_.serializers import LinkSerializer, UserSerializer, ContactSerializer
from api_.models import Link, Contact
from api_.permissions import IsActive
from django.contrib.auth.models import User
from djoser.views import RegistrationView, LoginView


class CustomRegistrationView(RegistrationView):
    def get_serializer_class(self):
        return UserSerializer

class CustomLoginView(LoginView):
    
    permission_classes = (IsActive, )

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
