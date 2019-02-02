from django.contrib import admin
from users.models import User

#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
	model = User
	filter_horizontal = ('user_permissions', 'groups')
	list_display = ('username', 'email', 'first_name', 'last_name', )

admin.site.register(User, UserAdmin)