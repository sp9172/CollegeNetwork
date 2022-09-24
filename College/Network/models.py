
from django.db import models

# Create your models here.

# class bloodgroup(models.Model):
#     blood=models.CharField(max_length=10)
    
#     def __str__(self):
#         return self.blood


class PersonModel(models.Model):
    fname = models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.fname




class UserProfile(models.Model):
    mobile=models.CharField(max_length=15)
    avatar=models.ImageField(default='avatar.png', upload_to='Profile_Image')
    dateofbirth=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    # blood=models.ForeignKey(bloodgroup,on_delete=models.CASCADE)

class ImageUploading(models.Model):
    post=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')

class PostUploading(models.Model):
    postupload=models.CharField(max_length=200)

    
    