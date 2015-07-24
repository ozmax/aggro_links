from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    entry_date = models.DateTimeField()
    url = models.URLField(max_length=500)
    owner = models.ForeignKey(User)


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    owner = models.ForeignKey(User)

class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
