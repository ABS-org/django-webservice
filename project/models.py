# utf-8
from django.db import models
from project import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django_facebook.utils import get_user_model, get_profile_model


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class MyCustomProfile(FacebookModel):
		user = models.OneToOneField(settings.AUTH_USER_MODEL)
		@receiver(post_save)
		def create_profile(sender, instance, created, **kwargs):

				if sender == get_user_model():

						user = instance
						profile_model = get_profile_model()

				if profile_model == MyCustomProfile and created:

						profile, new = MyCustomProfile.objects.get_or_create(user=instance)