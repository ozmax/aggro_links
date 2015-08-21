import datetime

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from api_.models import Link, Category, Contact, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
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
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.create(owner=user, **validated_data)
        return category


class CategoryListingField(serializers.RelatedField):

    def to_representation(self, value):
        user = self.context['view'].request.user
        if value.owner == user and isinstance(value, Category):
            serializer = CategorySerializer(value)
            return serializer.data

    def to_internal_value(self, data):
        user = self.context['view'].request.user
        if data:
            try:
                cat = Category.objects.get(id=int(data), owner=user )
            except Category.DoesNotExist:
                cat = None
        return cat


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
        link = Link.objects.create(owner=user,
                                   entry_date=entry_date,
                                   **validated_data)
        if cats:
            for cat in cats:
                if cat:
                    link.categories.add(cat)
        return link


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', )
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = self.context['request'].user
        group = Group.objects.create(owner=user, **validated_data)
        return group


class GroupListingField(serializers.RelatedField):

    def to_representation(self, value):
        user = self.context['view'].request.user
        if value.owner == user and isinstance(value, Group):
            serializer = GroupSerializer(value)
            return serializer.data

    def to_internal_value(self, data):
        groups = []
        if data:
            for id in data.split(','):
                gr = Group.objects.filter(id=int(id))
                if gr:
                    groups.append(gr[0])
        return groups


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupListingField(
        queryset=Group.objects.all(),
        many=True,
        required=False,
    )
    email = serializers.EmailField()

    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email', 'groups')

    def create(self, validated_data):
        if 'groups' in validated_data:
            groups = validated_data.pop('groups')
        user = self.context['request'].user
        contact = Contact.objects.create(owner=user, **validated_data)
        if groups:
            for gr in groups[0]:
                contact.groups.add(gr)
        return contact
