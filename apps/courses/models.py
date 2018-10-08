# _*_ encoding:utf-8 _*_
from django.db import models

from datetime import datetime
# Create your models here.


class Course(models.Model):
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name="课程难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")),
                              max_length=2)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    image = models.ImageField(verbose_name="封面图", upload_to="courses/%Y/%m", max_length=100)
    click_num = models.IntegerField(verbose_name="点击数", default=0)
    add_time = models.DateField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节名")
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(verbose_name="资源文件", upload_to="course/resource/%Y/%m", max_length=100)
    add_time = models.DateField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


