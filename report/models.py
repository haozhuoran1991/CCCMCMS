from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField

# Create your models here.
@python_2_unicode_compatible
class report(models.Model):
    title = models.CharField('標題', max_length=256)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '報告'
        verbose_name_plural = '報告'