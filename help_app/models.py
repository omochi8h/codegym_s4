from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Parents(AbstractUser):
    name = models.CharField(
        verbose_name='名前',
        max_length=20,
        blank=False,
        null=False
    )

    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    password = models.TextField(
        verbose_name='パスワード',
        blank=False,
        null=False
    )

    authcode = models.CharField(
        verbose_name='認証コード',
        max_length=20,
        blank=False,
        null=True
    )

    # icon = models.ImageField(
    #     upload_to="media/",
    #     blank=False,
    #     null=True
    # )

    def __str__(self):
        return self.name


class Children(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=20,
        blank=False,
        null=False
    )

    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE

    )

    def __str__(self):
        return self.name



class Houseworks(models.Model):
    job_name = models.CharField(
        verbose_name='お手伝い名',
        max_length=20,
        blank=False,
        null=False
    )

    point = models.IntegerField(
        verbose_name='ポイント',
        blank=False,
        null=True
    )

    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.job_name

class Tasks(models.Model):
    child = models.ForeignKey(
        Children,
        on_delete=models.CASCADE
    )

    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )

    work = models.ForeignKey(
        Houseworks,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        blank=False,
        null=False
    )

    state = models.IntegerField(
        default=0,
        blank=False,
        null=False
    )

    comment = models.CharField(
        verbose_name='コメント',
        max_length=50,
        blank=False,
        null=True
    )


class days_comment(models.Model):
    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        blank=False,
        null=False
    )

    comment = models.TextField(
        verbose_name='コメント',
        blank=False,
        null=False
    )