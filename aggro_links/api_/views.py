from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from api_.serializers import LinkSerializer, UserSerializer, ContactSerializer
from api_.models import Link, Contact
from django.contrib.auth.models import User

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        print 'hii'
        from rest_framework.response import Response
        if request.user:
            queryset = [user]
            return Response(queryset)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
