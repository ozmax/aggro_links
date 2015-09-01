from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from djoser.views import RegistrationView, RootView, UserView

from api_.models import Link, Contact, Category, Group
from api_.metadata import LinkMetaData
from api_.serializers import LinkSerializer, UserSerializer,UpdateUserSerializer, \
    ContactSerializer, CategorySerializer, GroupSerializer


class CustomRegistrationView(RegistrationView):
    def get_serializer_class(self):
        return UserSerializer


class CustomUserView(UserView):

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.request.method == "PUT" or\
            self.request.method == "PATCH":
            return UpdateUserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()


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
