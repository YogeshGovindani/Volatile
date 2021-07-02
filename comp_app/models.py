from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contest(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
