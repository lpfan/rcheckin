import uuid

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    qr_code_hash = models.UUIDField(default=uuid.uuid4, unique=True)


class Journal(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(blank=True, null=True)
