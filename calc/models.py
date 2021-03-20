from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Destination(models.Model):
    title = models.CharField(max_length=100)
    imgurl = models.TextField()
    desc = models.TextField()
    author = models.ForeignKey(User , blank=True, null=True, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    isrelated = models.ForeignKey(Destination, on_delete=models.CASCADE)