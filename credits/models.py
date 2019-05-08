from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='accounts', on_delete=models.CASCADE
    )


class Profile(models.Model):
    """
    For testing, track the number of "credits".
    """
    user = models.OneToOneField(
        'auth.User', related_name='profile', on_delete=models.CASCADE
    )
    credits = models.PositiveIntegerField(default=0)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)


def user_post_save(sender, instance, created, raw, **kwargs):
    if created:
        Profile.objects.create(user=instance)
models.signals.post_save.connect(user_post_save, sender=User)
