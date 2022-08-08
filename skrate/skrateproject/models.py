from django.db import models
# Create your models here.
class User(models.Model):
    #check in html how to limit username characters
    username = models.TextField()
    role = models.CharField(max_length=8,default='')
    auth_key = models.TextField()

class Ticket(models.Model):
    title = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=5,default='')
    priority = models.CharField(max_length=6,default='')
    assignedTo = models.TextField()
    createdAt = models.DateTimeField(default='')
