from django.db import models


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
        verbose_name = 'Хэштеги'
        verbose_name_plural = 'Хэштег'


class Moods(models.Model):
    mood_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Настроение')

    def __str__(self):
        return str(self.mood_name)

    class Meta:
        verbose_name = 'Настроения'
        verbose_name_plural = 'Настроение'


class Country(models.Model):
    country_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')

    def __str__(self):
        return str(self.country_name)

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страна'


class Track(models.Model):
    file = models.FileField(null=True, blank=True, upload_to="mp4", verbose_name='Трэк')
    photo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Фото')
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    track_length = models.IntegerField(null=True, blank=True, verbose_name='Длительность трека')
    sports_name = models.ForeignKey(Sports, on_delete=models.CASCADE, verbose_name='Наименование спорта')
    tag_name = models.ManyToManyField('Tags', verbose_name='Хэштег')
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
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=256, null=True, blank=True, verbose_name='E-Mail')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    price = models.IntegerField(null=True, blank=True, verbose_name='Стоимость')

    def __str__(self):
        return str(self.order_number)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

