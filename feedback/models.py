from django.contrib.auth.models import User
from django.db import models


class TicketStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class TicketCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


from django.db import models

# Create your models here.
