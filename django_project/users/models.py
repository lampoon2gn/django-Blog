from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  image = models.ImageField(default='default.jpg',upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'
  
  def save(self):
    super().save() #! run save method of the parent class

    img = Image.open(self.image.path) #! use pillow to open the target image
    
    if img.height > 300 or img.width >300: #! if image too large, resize and overwrite to save space and performance
      output_size = (300,300)
      img.thumbnail(output_size)
      img.save(self.image.path)