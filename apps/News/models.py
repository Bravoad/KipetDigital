from django.db import models


class News(models.Model):
    name = models.CharField('Наименование', max_length=250, default='')
    description = models.TextField('Описание проекта')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['order', ]
