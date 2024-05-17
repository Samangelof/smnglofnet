from django.db import models
from auths.models import UserNet
from apps.chat_groups.models import GroupChat

class MainGroup(models.Model):
    ...


class PostGroup(models.Model):
    name_group = models.ForeignKey(GroupChat, on_delete=models.CASCADE, verbose_name="Заголовок группы")
    text = models.CharField(max_length=1000, verbose_name="Текст", null=True, blank=False)
    image = models.FileField(verbose_name="Изображение", null=True, blank=True)

    contacts = models.ManyToManyField(UserNet)

    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self) -> str:
        return '{}: {}'.format(self.author, self.text) 

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('date_create',)