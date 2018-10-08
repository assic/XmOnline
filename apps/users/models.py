# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# 继承django默认的用户表并加入字段
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(verbose_name=u"性别", choices=(("male", u"男"), ("female", u"女")),
                              default="female", max_length=7)
    address = models.CharField(verbose_name=u"地址", max_length=100, default="")
    mobile = models.CharField(verbose_name=u"联系方式", max_length=11, null=True, blank=True)
    image = models.ImageField(verbose_name=u"头像", upload_to="image/%Y/%m", default="image/default.png",
                              max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name="验证码", max_length=20)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")),
                                 max_length=10, verbose_name="验证码类型")
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(verbose_name="轮播图片", upload_to="banner/%Y/%m",max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问链接")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name