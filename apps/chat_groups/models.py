from django.db import models
from auths.models import UserNet


class GroupChat(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Беседа'
        verbose_name_plural = 'Беседы'
        ordering = ['name']

    def __str__(self):
        return self.name


class UserSendMessageInGroup(models.Model):
    user_sender = models.ForeignKey(
        UserNet, 
        on_delete=models.CASCADE, 
        verbose_name='От пользователя', 
        related_name='sender_group'
    )

    message = models.TextField(max_length=1200)
    receiver_group = models.ManyToManyField(GroupChat)

    class Meta:
        verbose_name = 'Сообщение в беседу'
        verbose_name_plural = 'Сообщение в беседы'
        ordering = ['message']

    def __str__(self):
        return '{}: {} | {}'.format(self.user_sender, self.message, self.receiver_group.name
        
        )

