
from __future__ import unicode_literals
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
# Create your models here


@python_2_unicode_compatible
class fellowship(models.Model):
    name = models.CharField("團契名稱", max_length = 256)
    slug = models.CharField('團契网址', max_length=256, db_index=True, unique=True)
    intro = UEditorField('團契簡介', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse(
            'fellowship', args=(self.slug,)
        )

    class Meta:
        verbose_name='團契'
        verbose_name_plural = '團契'
        ordering = [ 'name' ]