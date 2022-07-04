# Generated by Django 4.0.4 on 2022-07-04 16:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('subscription', models.BooleanField(default=False, verbose_name='Подписан?')),
                ('subscription_email', models.EmailField(blank=True, max_length=256, null=True, verbose_name='Почта подписки')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdBigPhotoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='ad_big_photo_images/', verbose_name='Фото')),
                ('ad_period', models.DateField(blank=True, null=True, verbose_name='Срок рекламы')),
                ('published', models.BooleanField(verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Большая реклама',
                'verbose_name_plural': 'Большие рекламы',
            },
        ),
        migrations.CreateModel(
            name='AdSmallPhotoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='ad_small_photo_images/', verbose_name='Фото')),
                ('ad_period', models.DateField(blank=True, null=True, verbose_name='Срок рекламы')),
                ('published', models.BooleanField(verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Маленькая реклама',
                'verbose_name_plural': 'Маленькие рекламы',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Купон')),
                ('validity_period', models.DateField(blank=True, null=True, verbose_name='Срок действия')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
                ('percent', models.IntegerField(blank=True, null=True, verbose_name='Процент')),
            ],
            options={
                'verbose_name': 'Купон',
                'verbose_name_plural': 'Купоны',
            },
        ),
        migrations.CreateModel(
            name='DirectionEffect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_effect', models.CharField(blank=True, max_length=64, null=True, verbose_name='Направление воздействияэффекта')),
            ],
            options={
                'verbose_name': 'Направление воздействия эффекта',
                'verbose_name_plural': 'Направления воздействий эффектов',
            },
        ),
        migrations.CreateModel(
            name='DirectionMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_music', models.CharField(blank=True, max_length=64, null=True, verbose_name='Направление музыки')),
            ],
            options={
                'verbose_name': 'Направление музыки',
                'verbose_name_plural': 'Направления музыки',
            },
        ),
        migrations.CreateModel(
            name='Moods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Настроение')),
            ],
            options={
                'verbose_name': 'Настроение',
                'verbose_name_plural': 'Настроения',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderSegmentAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_add_begin', models.TimeField(blank=True, null=True, verbose_name='Начало хронометража')),
                ('time_add_end', models.TimeField(blank=True, null=True, verbose_name='Конец хронометража')),
                ('time_insert', models.TimeField(blank=True, null=True, verbose_name='Вставить в')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Таймер добавления',
                'verbose_name_plural': 'Таймеры добавлений',
            },
        ),
        migrations.CreateModel(
            name='OrderSegmentDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_delete_begin', models.TimeField(blank=True, null=True, verbose_name='Начало хронометража')),
                ('time_delete_end', models.TimeField(blank=True, null=True, verbose_name='Конец хронометража')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Таймер удаления',
                'verbose_name_plural': 'Таймеры удалений',
            },
        ),
        migrations.CreateModel(
            name='PaymentIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название способа оплаты')),
                ('icon', models.ImageField(upload_to='payment_icons/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Способы оплаты(иконки)',
                'verbose_name_plural': 'Способы оплаты(иконки)',
            },
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Наименование спорта')),
            ],
            options={
                'verbose_name': 'Вид спорта',
                'verbose_name_plural': 'Виды спорта',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Хэштег')),
            ],
            options={
                'verbose_name': 'Хэштег',
                'verbose_name_plural': 'Хэштеги',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='mp4', verbose_name='Трэк')),
                ('photo', models.ImageField(upload_to='track_images/', verbose_name='Фото')),
                ('author', models.CharField(blank=True, max_length=150, null=True, verbose_name='Автор')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название трека')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('track_length', models.IntegerField(blank=True, null=True, verbose_name='Длительность')),
                ('with_words', models.BooleanField(default=False, verbose_name='Со словами?')),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.country', verbose_name='Страна')),
                ('direction_music', models.ManyToManyField(to='muzsport.directionmusic', verbose_name='Направление музыки')),
                ('mood_name', models.ManyToManyField(to='muzsport.moods', verbose_name='Настроение')),
                ('sports_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.sports', verbose_name='Вид спорта')),
                ('tag_name', models.ManyToManyField(blank=True, null=True, to='muzsport.tags', verbose_name='Хэштег')),
                ('variants', models.ManyToManyField(blank=True, null=True, to='muzsport.track', verbose_name='Версии песни')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
        migrations.CreateModel(
            name='UnloadingModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка на файл')),
                ('file', models.FileField(blank=True, null=True, upload_to='mp4', verbose_name='Дополнительный файл')),
                ('direction_effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.directioneffect', verbose_name='Направление воздействияэффекта')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Разгрузочный модуль',
                'verbose_name_plural': 'Разгрузочный модуль',
            },
        ),
        migrations.CreateModel(
            name='TrackModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Начало хронометража')),
                ('time_stop', models.TimeField(verbose_name='Конец хронометража')),
                ('beginning_peak', models.BooleanField(verbose_name='Пик в начале')),
                ('end', models.BooleanField(verbose_name='Окончание')),
                ('commentary', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Комментарий к заказу')),
                ('order_segment_add', models.ManyToManyField(to='muzsport.ordersegmentadd', verbose_name='Добавление сегмента')),
                ('order_segment_delete', models.ManyToManyField(to='muzsport.ordersegmentdelete', verbose_name='Удаление сегмента')),
                ('sports_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.sports', verbose_name='Вид спорта')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.track', verbose_name='Трек')),
            ],
            options={
                'verbose_name': 'Доработать трек',
                'verbose_name_plural': 'Доработать трек',
            },
        ),
        migrations.CreateModel(
            name='SuggestiveEffect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя спортсмена')),
                ('file', models.FileField(blank=True, null=True, upload_to='mp4', verbose_name='Дополнительный файл')),
                ('direction_effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.directioneffect', verbose_name='Направление воздействияэффекта')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Суггестивный эффект',
                'verbose_name_plural': 'Суггестивные эффекты',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='track',
            field=models.ManyToManyField(to='muzsport.track', verbose_name='Заказ трека'),
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_count_start', models.IntegerField(default=2021, null=True, verbose_name='С какого года')),
                ('year_count_end', models.IntegerField(default=2022, null=True, verbose_name='По какой год')),
                ('link_icon', models.BooleanField(default=True, verbose_name='Отображение иконки со ссылкой')),
                ('payment_icons', models.ManyToManyField(to='muzsport.paymenticons', verbose_name='Способы оплаты')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футеры',
            },
        ),
        migrations.CreateModel(
            name='CustomTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Начало хронометража')),
                ('time_stop', models.TimeField(verbose_name='Конец хронометража')),
                ('beginning_peak', models.BooleanField(verbose_name='Пик в начале')),
                ('end', models.BooleanField(verbose_name='Окончание')),
                ('link', models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка на файл')),
                ('file', models.FileField(blank=True, null=True, upload_to='mp4', verbose_name='Файл (MP3)')),
                ('commentary', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Комментарий к заказу')),
                ('order_segment_add', models.ManyToManyField(to='muzsport.ordersegmentadd', verbose_name='Добавление сегмента')),
                ('order_segment_delete', models.ManyToManyField(to='muzsport.ordersegmentdelete', verbose_name='Удаление сегмента')),
                ('sports_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.sports', verbose_name='Вид спорта')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.track', verbose_name='Трек из каталога')),
            ],
            options={
                'verbose_name': 'Индивидуальный трек',
                'verbose_name_plural': 'Индивидуальные треки',
            },
        ),
        migrations.CreateModel(
            name='AddTrackToTheProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка на файл')),
                ('file', models.FileField(blank=True, null=True, upload_to='mp4', verbose_name='Файл (MP3)')),
                ('commentary', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Комментарий к заказу')),
                ('order_segment_add', models.ManyToManyField(to='muzsport.ordersegmentadd', verbose_name='Добавление сегмента')),
                ('order_segment_delete', models.ManyToManyField(to='muzsport.ordersegmentdelete', verbose_name='Удаление сегмента')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.track', verbose_name='Трек из каталога')),
            ],
            options={
                'verbose_name': 'Добавить трек к программе',
                'verbose_name_plural': 'Добавить трек к программе',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wished_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzsport.track')),
            ],
            options={
                'verbose_name': 'Закладка',
                'verbose_name_plural': 'Закладки',
                'unique_together': {('user', 'wished_track')},
            },
        ),
    ]
