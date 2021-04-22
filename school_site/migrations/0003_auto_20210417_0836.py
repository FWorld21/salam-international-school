# Generated by Django 3.2 on 2021-04-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_site', '0002_alter_teachers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='surname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Фото'),
        ),
    ]