# Generated by Django 5.2.2 on 2025-06-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование контакта')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Контактная форма',
                'verbose_name_plural': 'Контактные формы',
            },
        ),
    ]
