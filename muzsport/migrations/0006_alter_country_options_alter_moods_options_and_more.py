# Generated by Django 4.0.4 on 2022-05-24 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzsport', '0005_alter_track_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='moods',
            options={'verbose_name': 'Настроение', 'verbose_name_plural': 'Настроения'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Хэштег', 'verbose_name_plural': 'Хэштегb'},
        ),
    ]