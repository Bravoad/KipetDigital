from django.db import models


class TypeProject(models.Model):
    name = models.CharField('Наименование', max_length=250, default='')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Тип проекта'
        verbose_name_plural = 'Типы проектов'
        ordering = ['order', ]


class Project(models.Model):
    name = models.CharField('Наименование', max_length=250, default='')
    typeProject = models.ForeignKey(TypeProject,on_delete=models.CASCADE)
    description = models.TextField('Описание проекта')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['order', ]
