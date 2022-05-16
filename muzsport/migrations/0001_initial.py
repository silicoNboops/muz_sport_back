# Generated by Django 4.0.4 on 2022-05-15 09:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validity_period', models.CharField(blank=True, max_length=20, null=True, verbose_name='Срок действия')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер заказа')),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=150, null=True, verbose_name='Автор')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название трека')),
                ('sport_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Вид спорта')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('beginning_peak', models.BooleanField(default=True, verbose_name='Пик в начале')),
                ('sportsman_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя спортсмена')),
                ('photo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фото')),
                ('track_length', models.IntegerField(blank=True, null=True, verbose_name='Длительность трека')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('coupons', models.CharField(blank=True, max_length=30, null=True, verbose_name='Купоны')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
