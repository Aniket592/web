from django.db import models

# Create your models here.


class Spacians(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile_no = models.CharField(max_length=10,default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=25,default='')
    age = models.PositiveIntegerField()


    def __str__(self):
        return self.name