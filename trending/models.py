from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Trending(models.Model):
    
    title = models.CharField(default="#",max_length=300)

    def __str__(self):
        return self.title
