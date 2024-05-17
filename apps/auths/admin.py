from django.contrib import admin
from .models import UserNet


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff',)
    list_filter = ('username',)


admin.site.register(UserNet, UserAdmin)