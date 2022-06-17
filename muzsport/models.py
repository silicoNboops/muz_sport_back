from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Sports(models.Model):
    sports_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Наименование спорта')

    def __str__(self):
        return str(self.sports_name)

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'


class Tags(models.Model):
    tag_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Хэштег')

    def __str__(self):
        return str(self.tag_name)

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


# class Subscribe(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     subscription = models.BooleanField(default=False, verbose_name="Подписан?")
#     subscription_email = models.EmailField(max_length=256, blank=True, null=True, verbose_name="Почта подписки")
#
#     def __str__(self):
#         return str(self.user)
#
#     class Meta:
#         verbose_name = 'Подписка'
#         verbose_name_plural = 'Подписки'


class User(AbstractUser):
    subscription = models.BooleanField(default=False, verbose_name="Подписан?")
    subscription_email = models.EmailField(max_length=256, blank=True, null=True, verbose_name="Почта подписки")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class DirectionEffect(models.Model):
    direction_effect_name = models.CharField(max_length=64, null=True, blank=True, verbose_name='Направление воздействия'
                                                                                                'эффекта')

    def __str__(self):
        return str(self.direction_effect_name)

    class Meta:
        verbose_name = 'Направление воздействия эффекта'
        verbose_name_plural = 'Направления воздействий эффектов'


class Moods(models.Model):
    mood_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Настроение')

    def __str__(self):
        return str(self.mood_name)

    class Meta:
        verbose_name = 'Настроение'
        verbose_name_plural = 'Настроения'


class Country(models.Model):
    country_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')

    def __str__(self):
        return str(self.country_name)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Track(models.Model):
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Трэк')
    photo = models.ImageField(upload_to='track_images/', height_field=None, width_field=None, verbose_name='Фото')
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    track_length = models.IntegerField(null=True, blank=True, verbose_name='Длительность трека')
    sports_name = models.ForeignKey(Sports, on_delete=models.CASCADE, verbose_name='Наименование спорта')
    tag_name = models.ManyToManyField('Tags', verbose_name='Хэштег', )
    mood_name = models.ManyToManyField('Moods', verbose_name='Настроение')
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    with_words = models.BooleanField(default=False, verbose_name='Со словами?')

    def __str__(self):
        return f"{self.title}-{self.author}"

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'


class Coupons(models.Model):
    coupon_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Купон', unique=True)
    validity_period = models.DateField(null=True, blank=True, verbose_name='Срок действия')
    status = models.BooleanField(default=True, verbose_name='Статус')
    percent = models.IntegerField(null=True, blank=True, verbose_name='Процент')

    def __str__(self):
        return f"{self.coupon_name}"

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Order(models.Model):
    time_begin = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                   verbose_name='Начало хронометража')
    time_end = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                 verbose_name='Конец хронометража')
    beginning_peak = models.BooleanField(verbose_name='Пик в начале')
    ending = models.BooleanField(verbose_name='Окончание плавное') # плавное или резкое
    is_auto_layout = models.BooleanField(verbose_name='Автоматическая компоновка?')  # Авто или ручное
    comment_for_product = models.CharField(max_length=250, verbose_name='Комментарий к продукту', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderSegmentDelete(models.Model):
    time_delete_begin = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                         verbose_name='Начало хронометража')
    time_delete_end = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                         verbose_name='Конец хронометража')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Таймер удаления'
        verbose_name_plural = 'Таймеры удалений'


class OrderSegmentAdd(models.Model):
    time_add_begin = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                       verbose_name='Начало хронометража')
    time_add_end = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                     verbose_name='Конец хронометража')
    time_insert = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                    verbose_name='Вставить в')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Таймер добавления'
        verbose_name_plural = 'Таймеры добавлений'


class AdBigPhotoFile(models.Model):
    photo = models.ImageField(upload_to='ad_big_photo_images/', height_field=None, width_field=None, verbose_name='Фото')
    ad_period = models.DateField(null=True, blank=True, verbose_name='Срок рекламы')
    published = models.BooleanField(verbose_name='Опубликовано')

    def __str__(self):
        return str(self.ad_period)

    class Meta:
        verbose_name = 'Большая реклама'
        verbose_name_plural = 'Большие рекламы'


class AdSmallPhotoFile(models.Model):
    photo = models.ImageField(upload_to='ad_small_photo_images/', height_field=None, width_field=None,
                              verbose_name='Фото')
    ad_period = models.DateField(null=True, blank=True, verbose_name='Срок рекламы')
    published = models.BooleanField(verbose_name='Опубликовано')

    def __str__(self):
        return str(self.ad_period)

    class Meta:
        verbose_name = 'Маленькая реклама'
        verbose_name_plural = 'Маленькие рекламы'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Закладки'
        verbose_name_plural = 'Закладки'
        unique_together = (('user', 'wished_track'),)

    def __str__(self):
        return f"{self.user} {self.wished_track}"


class SuggestiveEffect(models.Model):
    athlete_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="Имя спортсмена")
    direction_effect = models.ForeignKey(DirectionEffect, on_delete=models.CASCADE, verbose_name='Направление воздействия'
                                                                                                 'эффекта')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Дополнительный файл')

    def __str__(self):
        return str(self.athlete_name)

    class Meta:
        verbose_name = 'Суггестивный эффект'
        verbose_name_plural = 'Суггестивные эффекты'


class UnloadingModule(models.Model):
    direction_effect = models.ForeignKey(DirectionEffect, on_delete=models.CASCADE, verbose_name='Направление воздействия'
                                                                                    'эффекта')
    link = models.CharField(null=True, blank=True, max_length=512, verbose_name='Ссылка на файл')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Дополнительный файл')

    def __str__(self):
        return str(self.athlete_name)

    class Meta:
        verbose_name = 'Суггестивный эффект'
        verbose_name_plural = 'Суггестивные эффекты'

"""
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=256, null=True, blank=True, verbose_name='E-Mail')
"""