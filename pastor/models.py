from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
# Create your models here.

class pastor(models.Model):
    name = models.CharField("姓名",max_length=256)
    title = models.CharField("事工方向", max_length=256)
    social_account = models.CharField("社交賬號鏈接", max_length=256, default=u'')
    intro = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')


    class Meta:
        verbose_name='牧師'
        verbose_name_plural = '牧師'
        ordering = [ 'name' ]