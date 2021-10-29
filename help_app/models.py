from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Parents(AbstractUser):


    email = models.EmailField(
        verbose_name='メールアドレス',
        unique=True
    )

    authcode = models.CharField(
        verbose_name='認証コード(数字4桁)',
        max_length=20,
        blank=False,
        null=True
    )

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
        default=0,
        blank=False,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100000)]
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
        default=timezone.now,
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

class Days_comment(models.Model):
    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )

    comment = models.TextField(
        verbose_name='コメント',
        blank=False,
        null=False
    )


class Comment(models.Model):
    parent = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )

    child = models.ForeignKey(
        Children,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        default=timezone.now,
        blank=False,
        null=False
    )

    comment = models.TextField(
        verbose_name='コメント',
        blank=False,
        null=False
    )




