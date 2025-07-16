from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField('Наименование контакта',max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Контактная форма'
        verbose_name_plural = 'Контактные формы'
