from django.db import models

# Create your models here.
class theme(models.Model):
    title=models.CharField(max_length=256)
    content=models.CharField(max_length=256)

class daily_motto(models.Model):
    motto = models.TextField('每週選背經文',unique=True,default="耶和華賜人智慧，知識和聰明都由祂口")
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '每週背經'
        verbose_name_plural = '每週背經'


    def __str__(self):
        return self.motto



class SundaySchool(models.Model):
    name = models.CharField('課程名字', max_length=256)
    teacher = models.CharField('主講人',default='',max_length=256)
    classroom = models.CharField('教室', max_length=256)
    intro = models.TextField('課程簡介')


    class Meta:
        verbose_name = '主日學'
        verbose_name_plural = '主日學'