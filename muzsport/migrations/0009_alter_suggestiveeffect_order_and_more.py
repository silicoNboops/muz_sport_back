# Generated by Django 4.0.4 on 2022-07-08 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muzsport', '0008_addtracktotheprogram_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestiveeffect',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='muzsport.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='suggestiveeffect',
            name='track_modification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='muzsport.trackmodification', verbose_name='Доработка трека'),
        ),
    ]
