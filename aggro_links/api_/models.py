from django.contrib.auth.models import User
from django.db import models

class Link(models.Model):
    entry_date = models.DateField()
    text = models.CharField(max_length=350)

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_owner = models.ForeignKey(User)
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    contacts = 
'''
