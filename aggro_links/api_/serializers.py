import datetime

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api_.models import Link, Category, Contact


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



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.create(owner=user, **validated_data)
        return category


class LinkSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    #categories = CategorySerializer(many=True)
    class Meta:
        model = Link
        fields = ('id', 'entry_date', 'url', 'categories')
        read_only_fields = ('entry_date', )

    def create(self, validated_data):
        user = self.context['request'].user
        entry_date = datetime.datetime.now()
        link = Link.objects.create(owner=user, entry_date=entry_date, **validated_data)
        return link

    def get_categories(self, obj):
        owner = obj.owner
        queryset = obj.categories
        serializer = CategorySerializer(queryset, many=True)
        return serializer.data


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email')

    def create(self, validated_data):
        user = self.context['request'].user
        contact = Contact.objects.create(owner=user, **validated_data)
        return contact
