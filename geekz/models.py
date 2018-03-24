# coding=utf-8
from django.contrib import admin
from django.db import models


class Pair(models.Model):
    word = models.CharField(max_length=16, verbose_name='Слово')
    synonym = models.CharField(max_length=16, verbose_name='Синоним')

    class Meta:
        verbose_name = u'Пара'
        verbose_name_plural = u'Пары слов'


class PairAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'synonym')
    search_fields = ('word', 'synonym')

admin.site.register(Pair, PairAdmin)
