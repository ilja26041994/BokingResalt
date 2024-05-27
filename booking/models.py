from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ManyToManyField(Room)
    check_in = models.DateField()
    check_out = models.DateField()
    description = models.TextField()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)