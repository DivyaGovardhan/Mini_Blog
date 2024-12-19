from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=200, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(max_length=200, verbose_name='Email', unique=True)
    password = models.CharField(max_length=200, verbose_name='Пароль')
    avatar = models.FileField(verbose_name='Аватар', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()  # Содержимое поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время публикации

    def __str__(self):
        return self.title

    @property
    def comment_count(self):
        return self.comments.count()  # Предполагается, что у вас есть модель комментариев

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'