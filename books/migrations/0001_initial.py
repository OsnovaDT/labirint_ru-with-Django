# Generated by Django 3.1.2 on 2020-11-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('info', models.TextField(blank=True, help_text='Информация об авторе', null=True, verbose_name='Информация')),
                ('image', models.ImageField(blank=True, null=True, unique=True, upload_to='', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('info', models.TextField(blank=True, help_text='Информация об издательстве', null=True, verbose_name='Информация')),
                ('image', models.ImageField(blank=True, null=True, unique=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
                'ordering': ['name'],
            },
        ),
    ]