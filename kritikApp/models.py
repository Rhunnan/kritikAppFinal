from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=30)
    
class Establishment(models.Model):
    custom_id = models.AutoField(primary_key=True)
    path_image = models.CharField(max_length=255, blank=True, default='')
    name = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    ai_script = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

class Review(models.Model):
    custom_id = models.AutoField(primary_key=True)
    review_comment = models.TextField(blank=True, default='')
    star_rating = models.FloatField(default=0)
    image_path = models.CharField(max_length=255, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True) # ForeignKey to User or ID
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, null = True) # ForeignKey to Establishment or ID

    def __str__(self):
        return self.name
    