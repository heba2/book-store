from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from book.models import Book

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Book, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

    if user_profile.stripe_id is None or user_profile.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=instance.email)
        user_profile.stripe_id = new_stripe_id['id']
        user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
