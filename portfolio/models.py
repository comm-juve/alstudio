# coding: utf-8
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название видео')
    video_code = models.TextField(null=True, blank=True, verbose_name=u'Код видео')

    class Meta:
        verbose_name = u'Портфолио'
        verbose_name_plural = u'Портфолио'
        db_table = 'portfolio'
