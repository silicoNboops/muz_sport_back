from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Sports(models.Model):
    sports_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Наименование спорта')
    sports_name_en = models.CharField(max_length=30, null=True, blank=True, verbose_name='Наименование спорта(EN)')

    def __str__(self):
        return str(self.sports_name)

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'


class PriceModificationAndServices(models.Model):
    price_finished_track = models.IntegerField(verbose_name='Цена доработки трека')
    price_additional_track = models.IntegerField(verbose_name='Цена добавления трека к программе')
    price_suggestive_effect = models.IntegerField(verbose_name='Цена суггестивного эффекта')
    price_unloading_module = models.IntegerField(verbose_name='Цена разгрузочного модуля')
    sports_programme_min = models.IntegerField(verbose_name='Цена спортивной программы(минимальный тариф)')
    sports_programme_medium = models.IntegerField(verbose_name='Цена спортивной программы(средний тариф)')
    sports_programme_max = models.IntegerField(verbose_name='Цена спортивной программы(максимальный тариф)')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Цены доработок и услуг'
        verbose_name_plural = 'Цены доработок и услуг'


class Tags(models.Model):
    tag_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Хэштег')
    tag_name_en = models.CharField(max_length=30, null=True, blank=True, verbose_name='Хэштег(EN)')

    def __str__(self):
        return str(self.tag_name)

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class User(AbstractUser):
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    subscription = models.BooleanField(default=False, verbose_name="Подписан?")
    subscription_email = models.EmailField(max_length=256, blank=True, null=True, verbose_name="Почта подписки")

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class DirectionEffect(models.Model):
    direction_effect = models.CharField(max_length=64, null=True, blank=True, verbose_name='Направление воздействия'
                                                                                                'эффекта')
    direction_effect_en = models.CharField(max_length=64, null=True, blank=True, verbose_name='Направление воздействия'
                                                                                           'эффекта(EN)')

    def __str__(self):
        return str(self.direction_effect)

    class Meta:
        verbose_name = 'Направление воздействия эффекта'
        verbose_name_plural = 'Направления воздействий эффектов'


class DirectionMusic(models.Model):
    direction_music = models.CharField(max_length=64, null=True, blank=True, verbose_name='Направление музыки')
    direction_music_en = models.CharField(max_length=64, null=True, blank=True, verbose_name='Направление музыки(EN)')

    def __str__(self):
        return str(self.direction_music)

    class Meta:
        verbose_name = 'Направление музыки'
        verbose_name_plural = 'Направления музыки'


class Moods(models.Model):
    mood_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Настроение')
    mood_name_en = models.CharField(max_length=30, null=True, blank=True, verbose_name='Настроение(EN)')

    def __str__(self):
        return str(self.mood_name)

    class Meta:
        verbose_name = 'Настроение'
        verbose_name_plural = 'Настроения'


class Country(models.Model):
    country_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    country_name_en = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна(EN)')

    def __str__(self):
        return str(self.country_name)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Track(models.Model):
    file = models.FileField(upload_to="mp4", verbose_name='Трек', max_length=5000)
    photo = models.ImageField(upload_to='track_images/', null=True, blank=True, height_field=None, width_field=None, verbose_name='Фото')
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    # TODO сделать формата 0:00/00:00
    # TODO задавать дефолтное значение исходя из длины прикрепленного аудио файла
    # TODO DurationField
    track_length = models.IntegerField(null=True, blank=True, default=0, verbose_name='Длительность')
    direction_music = models.ManyToManyField('DirectionMusic', verbose_name='Направление музыки',
                                             related_name='dir')
    sports_name = models.ForeignKey(Sports, on_delete=models.CASCADE, verbose_name='Вид спорта')
    tag_name = models.ManyToManyField('Tags', verbose_name='Хэштег', blank=True)
    mood_name = models.ManyToManyField('Moods', verbose_name='Настроение')
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    with_words = models.BooleanField(default=False, verbose_name='Со словами?')
    variants = models.ManyToManyField('self', blank=True, verbose_name='Версии песни')

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
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    track = models.ManyToManyField(Track, blank=True, verbose_name='Трек из каталога')
    track_custom = models.ManyToManyField('CustomTrack', blank=True,
                                          verbose_name='Индивидуальный заказ трека')
    track_modification = models.ManyToManyField('TrackModification', blank=True,
                                                verbose_name='Доработка трека',
                                                related_name='track_modifications')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.id}) {self.customer}. {self.time_create} - {self.time_update}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderSegmentDelete(models.Model):
    time_delete_begin = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                         verbose_name='Начало хронометража')
    time_delete_end = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                         verbose_name='Конец хронометража')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Таймер добавления'
        verbose_name_plural = 'Таймеры добавлений'


class TrackModification(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE,
                              verbose_name='Заказ')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name='Трек')
    sports_name = models.ForeignKey(Sports, on_delete=models.CASCADE, verbose_name='Вид спорта')
    time_start = models.TimeField(verbose_name='Начало хронометража')
    time_stop = models.TimeField(verbose_name='Конец хронометража')
    beginning_peak = models.BooleanField(verbose_name='Пик в начале')
    end = models.CharField(choices=(('smooth', 'Плавное'), ('sharp', 'Резкое')), default='smooth',
                           max_length=20, verbose_name='Окончание')
    composition = models.CharField(choices=(('auto', 'Авто'), ('manual', 'Ручная')), default='auto',
                                   max_length=20, verbose_name='Компоновка')
    order_segment_delete = models.ManyToManyField(OrderSegmentDelete, blank=True,
                                                  verbose_name='Удаление сегмента')
    order_segment_add = models.ManyToManyField(OrderSegmentAdd, blank=True,
                                               verbose_name='Добавление сегмента')
    # Добавление доп. трека к программе (макс. 2)
    additional_tracks = models.ManyToManyField('AddTrackToTheProgram', blank=True,
                                               verbose_name='Доп. треки к программе')
    suggestive_effect = models.ForeignKey('SuggestiveEffect', null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name='Суггестивный эффект')
    # TODO разгрузочный модуль
    commentary = models.CharField(max_length=1024, verbose_name='Комментарий к заказу', null=True,
                                  blank=True)
    # оплачен ли по итогу заказ
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    def __str__(self):
        return f'{self.id}: {self.track}'

    class Meta:
        verbose_name = 'Доработать трек'
        verbose_name_plural = 'Доработать трек'


class CustomTrack(models.Model):
    sports_name = models.ForeignKey(Sports, on_delete=models.CASCADE, verbose_name='Вид спорта')
    time_start = models.TimeField(verbose_name='Начало хронометража')
    time_stop = models.TimeField(verbose_name='Конец хронометража')
    beginning_peak = models.BooleanField(verbose_name='Пик в начале')
    end = models.BooleanField(verbose_name='Окончание')
    link = models.CharField(null=True, blank=True, max_length=512, verbose_name='Ссылка на файл')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Файл (MP3)')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name='Трек из каталога')
    order_segment_delete = models.ManyToManyField(OrderSegmentDelete, verbose_name='Удаление сегмента')
    order_segment_add = models.ManyToManyField(OrderSegmentAdd, verbose_name='Добавление сегмента')
    commentary = models.CharField(max_length=1024, verbose_name='Комментарий к заказу', null=True,
                                  blank=True)

    def __str__(self):
        return f'{self.sports_name} : {self.id}'

    class Meta:
        verbose_name = 'Индивидуальный трек'
        verbose_name_plural = 'Индивидуальные треки'


class AddTrackToTheProgram(models.Model):
    order = models.ForeignKey(Order, null=True, default=None, on_delete=models.CASCADE,
                              verbose_name='Заказ')
    track_modification = models.ForeignKey(TrackModification, null=True, default=None,
                                           on_delete=models.CASCADE, verbose_name='Доработка трека')
    link = models.CharField(null=True, blank=True, max_length=512, verbose_name='Ссылка на файл')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Файл (MP3)')
    track = models.ForeignKey(Track, null=True, blank=True, on_delete=models.CASCADE,
                              verbose_name='Трек из каталога')
    composition = models.CharField(choices=(('auto', 'Авто'), ('manual', 'Ручная')), default='auto',
                                   max_length=20, verbose_name='Компоновка')
    order_segment_delete = models.ManyToManyField(OrderSegmentDelete, blank=True,
                                                  verbose_name='Удаление сегмента')
    order_segment_add = models.ManyToManyField(OrderSegmentAdd, blank=True,
                                               verbose_name='Добавление сегмента')
    commentary = models.CharField(max_length=1024, verbose_name='Комментарий к заказу', null=True,
                                  blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Добавить трек к программе'
        verbose_name_plural = 'Добавить трек к программе'


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
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'
        unique_together = (('user', 'wished_track'),)

    def __str__(self):
        return f"{self.user}: {self.wished_track}"


class SuggestiveEffect(models.Model):
    athlete_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="Имя спортсмена")
    direction_effect = models.ForeignKey(DirectionEffect, on_delete=models.CASCADE,
                                         verbose_name='Направление воздействия эффекта')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Дополнительный файл')
    link = models.CharField(null=True, blank=True, max_length=512, verbose_name='Ссылка на файл')
    track_modification = models.ForeignKey(TrackModification, null=True, blank=True,
                                           on_delete=models.CASCADE, verbose_name='Доработка трека')
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE,
                              verbose_name='Заказ')

    def __str__(self):
        return f"{self.id}: {self.athlete_name} для Доработки {self.track_modification}"

    class Meta:
        verbose_name = 'Суггестивный эффект'
        verbose_name_plural = 'Суггестивные эффекты'


class UnloadingModule(models.Model):
    direction_effect = models.ForeignKey(DirectionEffect, on_delete=models.CASCADE, verbose_name='Направление воздействия'
                                                                                    'эффекта')
    link = models.CharField(null=True, blank=True, max_length=512, verbose_name='Ссылка на файл')
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Дополнительный файл')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Разгрузочный модуль'
        verbose_name_plural = 'Разгрузочный модуль'


class PaymentIcons(models.Model):
    title = models.CharField(verbose_name='Название способа оплаты', max_length=64)
    icon = models.ImageField(upload_to='payment_icons/', height_field=None, width_field=None, verbose_name='Иконка')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Способы оплаты(иконки)'
        verbose_name_plural = 'Способы оплаты(иконки)'


class Footer(models.Model):
    year_count_start = models.IntegerField(null=True, default=2021, verbose_name='С какого года')
    year_count_end = models.IntegerField(null=True, default=2022, verbose_name='По какой год')
    payment_icons = models.ManyToManyField(PaymentIcons, verbose_name='Способы оплаты')
    link_icon = models.BooleanField(default=True, verbose_name='Отображение иконки со ссылкой')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'
