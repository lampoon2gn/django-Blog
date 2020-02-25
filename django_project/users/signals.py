from django.db.models.signals import post_save
from django.contrib.auth.models import User #!sender of singal
from django.dispatch import receiver #! receiver receives signals and do something after
from .models import Profile


@receiver(post_save,sender=User)#! when user is created, send signal, the receiver is the create_profile function
def create_profile(sender,instance,created,**kwargs):
  if created:
    Profile.objects.create(user=instance)#!create profile when user is created

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
  instance.profile.save()#! save profile when user is saved