import datetime

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api_.models import Link, Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'username', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        Token.objects.create(user=user)
        return user


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'entry_date', 'url')
        read_only_fields = ('entry_date', )

    def create(self, validated_data):
        user = self.context['request'].user
        entry_date = datetime.datetime.now()
        link = Link.objects.create(user=user, entry_date=entry_date, **validated_data)
        return link

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email')
