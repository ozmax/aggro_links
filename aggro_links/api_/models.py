from django.db import models

class Link(models.Model):
    entry_date = models.DateField()
    text = models.CharField(max_length=350)
