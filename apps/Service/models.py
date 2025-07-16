from django.db import models

# Create your models here.


class Service (models.Model):
    name = models.CharField('Наименование услуги', max_length=250, default='')
    description = models.TextField('Описание услуги')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', ]

