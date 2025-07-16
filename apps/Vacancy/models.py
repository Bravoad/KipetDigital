from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profession(models.Model):
    name = models.CharField('Наименование', max_length=250, default='')
    is_displayed = models.BooleanField('Показать', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Желаемая должность'
        verbose_name_plural = 'Желаемые должности'


class Vacancy(models.Model):
    name = models.CharField('Наименование', max_length=250, default='')
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE)
    phone = PhoneNumberField('Номер телефона', help_text='Пример, +79510549236')
    email = models.EmailField()
    github = models.URLField('Ссылка на GITHUB')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
