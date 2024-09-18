from django.db import models

# Create your models here.

class courses(models.Model):
    name=models.CharField(max_length=30)
    des=models.TextField()
    image=models.ImageField(upload_to='images/')
    fee=models.IntegerField()
    offer=models.BooleanField(default=False)