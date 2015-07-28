from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from djoser.views import RegistrationView, RootView

from api_.models import Link, Contact, Category, Group
from api_.metadata import LinkMetaData
from api_.serializers import LinkSerializer, UserSerializer, \
    ContactSerializer, CategorySerializer, GroupSerializer


class CustomRegistrationView(RegistrationView):
    def get_serializer_class(self):
        return UserSerializer


class CustomRootView(RootView):

    urls_mapping = {}

    def get_urls_mapping(self, **kwargs):
        mapping = {}
        mapping.update(settings.ROOT_VIEW_URLS_MAPPING)
        return mapping

    def get(self, request, format=None):
        return Response(
            dict([(key, reverse(url_name, request=request, format=format))
                  for key, url_name in self.get_urls_mapping().items()])
        )


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    metadata_class = LinkMetaData


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    metadata_class = LinkMetaData


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
