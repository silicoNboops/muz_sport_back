# Generated by Django 4.0.4 on 2022-07-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzsport', '0011_suggestiveeffect_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_length',
            field=models.IntegerField(blank=True, null=True, verbose_name='Длительность'),
        ),
    ]
