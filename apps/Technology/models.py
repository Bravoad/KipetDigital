from django.db import models


class Technology(models.Model):
    name = models.CharField('Наименование', default='', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='uploads/%y%m%d')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', ]

