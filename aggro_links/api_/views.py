from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api_.serializers import LinkSerializer, UserSerializer, ContactSerializer
from api_.models import Link, Contact
from djoser.views import RegistrationView, RootView
from django.conf import settings
from rest_framework.reverse import reverse


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
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = Link.objects.filter(user=request.user)
        serializer = LinkSerializer(queryset, many=True)
        return Response(serializer.data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
