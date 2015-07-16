from rest_framework import viewsets
from api_.serializers import LinkSerializer, UserSerializer
from api_.models import Link
from django.contrib.auth.models import User
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
