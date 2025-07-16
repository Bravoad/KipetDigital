from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TypeService(models.Model):
    name = models.CharField('Наименование вида услуги', max_length=150)
    is_displayed = models.BooleanField('Показать вид услуги', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуг'

    def __str__(self):
        return f'{self.name}'


class Budget(models.Model):
    name = models.CharField('Примерная стоимость бюджета', max_length=150)
    is_displayed = models.BooleanField('Показать бюджет', default=True)
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        verbose_name = 'Бюджет на разработку'
        verbose_name_plural = 'Бюджеты на разработку'

    def __str__(self):
        return f'{self.name}'


class OrderService(models.Model):
    types_services = models.ManyToManyField(TypeService, related_name='types_services', blank=True)
    name = models.CharField('Имя отправителя', max_length=150)
    company = models.CharField('Компания или бренд', max_length=150)
    phone = PhoneNumberField('Номер телефона', blank=True, null=True, help_text='Пример, +79510549236')
    email = models.EmailField('Электронная почта')
    budget = models.ForeignKey(Budget, verbose_name='Бюджет на разработку', on_delete=models.CASCADE)
    comment = models.CharField('Комментарий',  blank=True, default='', max_length=150)
    file = models.FileField(verbose_name='Приложенный файл ТЗ',null=True)

    class Meta:
        verbose_name = 'Заказ услуги'
        verbose_name_plural = 'Заказ услуг'

    def __str__(self):
        return f'{self.name}'
