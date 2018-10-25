from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(verbose_name='姓名', max_length=30, null=True, blank=True, )
    birthday = models.DateField(verbose_name='出生年月', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', max_length=6, choices=[(0, '男'), (1, '女')], default=0)
    mobile = models.CharField(verbose_name='手机号', max_length=13)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(verbose_name='电话', max_length=11)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code