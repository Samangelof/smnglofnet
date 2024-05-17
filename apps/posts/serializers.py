from rest_framework import serializers
from .models import PostInPersonAccount, CommentOnPersonalAccount


class PostPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostInPersonAccount
        fields = ("author", "text", "image")


class CommentPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentOnPersonalAccount
        fields = ("author", "post", "text")