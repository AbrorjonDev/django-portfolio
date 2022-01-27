import os
from django.db.models.signals import post_delete, post_save
from .models import *
from django.dispatch import receiver

def _delete_image(path):
    if os.path.isfile(path):
        os.remove(path)

@receiver(post_delete, sender=Projects)
def project_image_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_delete, sender=Profile)
def profile_image_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)

