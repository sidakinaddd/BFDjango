from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser, UserProfile


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('created profile')
