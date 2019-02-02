from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from songr.models import PlaylistUpload, User

admin.site.register(PlaylistUpload)
admin.site.register(User, MPTTModelAdmin)
