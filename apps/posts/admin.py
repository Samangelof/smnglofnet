from django.contrib import admin

from .models import PostInPersonAccount, CommentOnPersonalAccount

admin.site.register(PostInPersonAccount)
admin.site.register(CommentOnPersonalAccount)
