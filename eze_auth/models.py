#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class EzeUserProfile(models.Model):
    user = models.ForeignKey(User)
    identity = models.CharField(max_length = 255)
    provider_code = models.CharField(max_length = 30)
    provider_name = models.CharField(max_length = 30)
    avatar_url = models.CharField(max_length = 255)
    preferred_username = models.CharField(max_length = 100, blank = True)
    display_name = models.CharField(max_length = 100, blank = True)
    name = models.CharField(max_length = 100, blank = True)
