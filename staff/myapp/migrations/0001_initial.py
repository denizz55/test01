# Generated by Django 5.0.1 on 2024-02-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('place', models.IntegerField(verbose_name='Количество')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='img', verbose_name='Фото')),
                ('square', models.CharField(max_length=100, verbose_name='Адрес заказа')),
            ],
            options={
                'verbose_name': 'Часы',
                'verbose_name_plural': 'Часы',
            },
        ),
    ]
