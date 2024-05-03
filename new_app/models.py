from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)

class Todont(models.Model):
    heading = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)