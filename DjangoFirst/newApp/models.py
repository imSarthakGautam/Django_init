from django.db import models
from django.utils import timezone

# Create your models here.

class userModel(models.Model):

    #enums
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHERS'),
    ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='imgModel/')
    # when you upload img Django will save in folder imgModel
    # install Pillow

    date_added = models.DateTimeField(default=timezone.now)
    sex=models.CharField(max_length=1, choices=GENDER)
    description= models.TextField(default='')

    def __str__(self):
        # to name userModel by own name
        return self.name



