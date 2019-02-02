from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	""" A class for the Dejay and User signup"""
	is_reveler = models.BooleanField(default=False)
	is_dejay   = models.BooleanField(default=False)

 