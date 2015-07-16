from django.contrib.auth.models import User

from rest_framework import serializers
from api_.models import Link

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'entry_date', 'text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)
