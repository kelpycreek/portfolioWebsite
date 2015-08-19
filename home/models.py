from django.db import models

# Create your models here.


class Drawing(models.Model):
  date = models.DateTimeField('date created')
  publishing = models.DateTimeField('date published to website')
  name = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to="home/static/images/%Y")
