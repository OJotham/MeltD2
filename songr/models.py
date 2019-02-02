from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils import timezone
from users.models import User
from django.urls import reverse

class User(User, MPTTModel):
    name = models.CharField(max_length=50, null=True, unique=True)
    parent = TreeForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='children', db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'users'

class PlaylistUpload(models.Model):
    song_file   = models.FileField(upload_to = 'videos/', null = True, verbose_name = "")
    date_posted = models.DateTimeField(default = timezone.now)
    dejay       = TreeForeignKey(User, null=True, on_delete=models.CASCADE, related_name='playlist')

    def __str__(self):
    	return str(self.song_file)

    def get_absolute_url(self):
    	return reverse('djroll-home')
