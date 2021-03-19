from django.db import models

# Create your models here.
class Destination(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    imgurl = models.TextField()
    desc = models.TextField()
