from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Link(models.Model):
    entry_date = models.DateTimeField()
    url = models.URLField(max_length=500)
    owner = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=False)


class Group(models.Model):
    group_name = models.CharField(max_length=150)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.group_name


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    owner = models.ForeignKey(User)
    group = models.ForeignKey(Group, null=True, blank=True)


