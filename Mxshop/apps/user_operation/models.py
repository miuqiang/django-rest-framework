from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from goods.models import Goods

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name