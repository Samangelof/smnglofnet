from django.contrib import admin
from .models import Follow


class FollowAdmin(admin.ModelAdmin):
    model = Follow
    raw_id_fields = ("follower", "followee")


admin.site.register(Follow, FollowAdmin)
