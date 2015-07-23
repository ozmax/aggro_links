from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    entry_date = models.DateTimeField()
    url = models.URLField(max_length=500)
    user = models.ForeignKey(User)


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_owner = models.ForeignKey(User)
