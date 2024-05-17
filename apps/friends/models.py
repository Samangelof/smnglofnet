from django.db import models
from django.utils import timezone
from django.core.cache import cache

from django.core.exceptions import ValidationError

from auths.models import UserNet
from friends.exceptions import AlreadyExistsError
from friends.signals import (
    followee_created,
    followee_removed,
    follower_created,
    follower_removed,
    following_created,
    following_removed,
)



BUST_CACHES = {
    "followers": ["followers"],
    "following": ["following"],
}

CACHE_TYPES = {
    "followers": "fo-%s",
    "following": "fl-%s",
}


def bust_cache(type, user_pk):
    """ Уничтожить кеш для данного типа """
    bust_keys = BUST_CACHES[type]
    keys = [CACHE_TYPES[k] % user_pk for k in bust_keys]
    cache.delete_many(keys)

def cache_key(type, user_pk):
    """ Создание ключа кеша для определенного типа кэшированного значения """
    return CACHE_TYPES[type] % user_pk


class FollowingManager(models.Manager):
    """ Менеджер подписок """

    def followers(self, user):
        """ Вернуть список всех подписчиков """
        key = cache_key("followers", user.pk)
        followers = cache.get(key)

        if followers is None:
            qs = Follow.objects.filter(followee=user).select_related("follower")
            followers = [u.follower for u in qs]
            cache.set(key, followers)

        return followers

    def following(self, user):
        """ Вернуть список всех пользователей, на которых подписан данный пользователь """
        key = cache_key("following", user.pk)
        following = cache.get(key)

        if following is None:
            qs = Follow.objects.filter(follower=user).select_related("followee")
            following = [u.followee for u in qs]
            cache.set(key, following)

        return following

    def add_follower(self, follower, followee):
        """ Создание подписки """
        if follower == followee:
            raise ValidationError("Пользователи не могут быть подписаны на самих себя")

        relation, created = Follow.objects.get_or_create(
            follower=follower, followee=followee
        )

        if created is False:
            raise AlreadyExistsError(
                f"Пользователь '{follower}' уже подписан на '{followee}'"
            )

        follower_created.send(sender=self, follower=follower)
        followee_created.send(sender=self, followee=followee)
        following_created.send(sender=self, following=relation)

        bust_cache("followers", followee.pk)
        bust_cache("following", follower.pk)

        return relation

    def remove_follower(self, follower, followee):
        """ Удаление подписки """
        try:
            rel = Follow.objects.get(follower=follower, followee=followee)
            follower_removed.send(sender=rel, follower=rel.follower)
            followee_removed.send(sender=rel, followee=rel.followee)
            following_removed.send(sender=rel, following=rel)
            rel.delete()
            bust_cache("followers", followee.pk)
            bust_cache("following", follower.pk)
            return True
        except Follow.DoesNotExist:
            return False

    def follows(self, follower, followee):
        """ Пользователь подписан, используем кеши """
        followers = cache.get(cache_key("following", follower.pk))
        following = cache.get(cache_key("followers", followee.pk))

        if followers and followee in followers:
            return True
        elif following and follower in following:
            return True
        else:
            return Follow.objects.filter(follower=follower, followee=followee).exists()


class Follow(models.Model):
    """ Модель для представления подписок """

    follower = models.ForeignKey(
        UserNet, models.CASCADE, related_name="following"
    )
    followee = models.ForeignKey(
        UserNet, models.CASCADE, related_name="followers"
    )
    created = models.DateTimeField(default=timezone.now)

    objects = FollowingManager()

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        unique_together = ("follower", "followee")

    def __str__(self):
        return f"Пользователь {self.follower} подписан на {self.followee}"
        # return f"Пользователь #{self.follower} подписан на #{self.followee_id}"

    def save(self, *args, **kwargs):
        """ Проверить что пользователь не подписан сам на себя """
        if self.follower == self.followee:
            raise ValidationError("Пользователи не могут быть подписаны на самих себя")
        super().save(*args, **kwargs)
