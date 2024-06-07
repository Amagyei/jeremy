from django.db import models
from shortuuid.django_fields import ShortUUIDField


# Create your models here.

class chicken(models.Model):
    chicen_image = models.ImageField(upload_to="chickens/"),
    chicken_id = ShortUUIDField(unique = True, length = 10, max_length=20, alphabet="abcdefghijklmnopqrstuvwxyz"),
    name = models.CharField(max_length=100, default="chicken",null=True )
    
class chicken_data_upload(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title