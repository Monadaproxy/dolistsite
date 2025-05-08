from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    picture = models.ImageField(upload_to='forum_images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение от {self.author.username}'
