from django.db import models
from auths.models import UserNet
from django.utils import timezone
from django.core.exceptions import ValidationError


class Messages(models.Model):
    sender = models.ForeignKey(UserNet, on_delete=models.CASCADE, verbose_name='От пользователя', related_name='sender')
    receiver = models.ForeignKey(UserNet, on_delete=models.CASCADE, verbose_name='Пользователю', related_name='receiver')
    message = models.TextField('Сообщение', max_length=1200)


    data_send = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Сообщение")
        verbose_name_plural = ("Сообщения")


    def __str__(self):
        return f"Пользователь {self.sender} отправил сообщение {self.receiver}"

    def save(self, *args, **kwargs):
        if self.sender == self.receiver:
            raise ValidationError("Пользователи не могут писать самим себе.")
        super().save(*args, **kwargs)