import datetime

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from api_.models import Link, Category, Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="This email is already registered.")]
        )
    
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
        fields = ('id', 'name', )
        read_only_fields = ('id')

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.create(owner=user, **validated_data)
        return category


class CategoryListingField(serializers.RelatedField):

    def to_representation(self, value):
        user = self.context['view'].request.user
        if value.owner==user and isinstance(value, Category):
            serializer = CategorySerializer(value)
            return serializer.data

    def to_internal_value(self, data):
        cats = []
        if data:
            for id in data.split(','):
                cat = Category.objects.filter(id=int(id))
                if cat:
                    cats.append(cat[0])
        return cats

class LinkSerializer(serializers.ModelSerializer):

    categories = CategoryListingField(
        queryset=Category.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Link
        fields = ('id', 'entry_date', 'url', 'categories')
        read_only_fields = ('id', 'entry_date', )

    def create(self, validated_data):
        if 'categories' in validated_data:
            cats = validated_data.pop('categories')
        user = self.context['request'].user
        entry_date = datetime.datetime.now()
        link = Link.objects.create(owner=user, entry_date=entry_date, **validated_data)
        if cats:
            for cat in cats[0]:
                link.categories.add(cat)
        return link

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email')

    def create(self, validated_data):
        user = self.context['request'].user
        contact = Contact.objects.create(owner=user, **validated_data)
        return contact
