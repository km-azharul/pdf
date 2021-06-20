from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50,blank=True)
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(null=True)
    priority = models.CharField(max_length=100,blank=True,null=True)
    assigned_to = models.EmailField(max_length=200,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title