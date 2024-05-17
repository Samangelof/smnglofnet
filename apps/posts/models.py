from django.db import models
from auths.models import UserNet


class PostInPersonAccount(models.Model):
    author = models.ForeignKey(UserNet, 
                                on_delete=models.CASCADE, 
                                verbose_name="Автор поста",
                                related_name='author_name')

    # models.TextField
    text = models.CharField(max_length=1000, verbose_name="Текст", null=True, blank=False)
    image = models.FileField(verbose_name="Изображение", null=True, blank=True)

    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self) -> str:
        return '{}: {}'.format(self.author, self.text) 

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('date_create',)




class CommentOnPersonalAccount(models.Model):
    author = models.ForeignKey(UserNet, on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(PostInPersonAccount, on_delete=models.CASCADE, verbose_name="Комментарий к посту")
    text = models.CharField(
        max_length=1000,
        verbose_name='Текст',
        null=False,
        blank=False     # blank=False : поле обязательное 
    ) 

    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        return '{}: {}'.format(self.author, self.text) 

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('date_create',)