from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class person(models.Model):
    fullname = models.CharField(max_length=100)
    
    