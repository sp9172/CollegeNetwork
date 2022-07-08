from django.db import models

# Create your models here.
class PersonModel(models.Model):
    fname = models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.fname
    
    