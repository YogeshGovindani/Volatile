from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contest(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    duration = models.IntegerField()


class Question(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    statement = models.CharField(max_length=500)
    input_cases = models.CharField(max_length=500)
    output_cases = models.CharField(max_length=500)
    points = models.IntegerField()

class Solution(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500)
    submitted_at = models.DateTimeField()
    verdict = models.BooleanField()