from django.db import models


class Track(models.Model):
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    sport_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Вид спорта')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    beginning_peak = models.BooleanField(default=True, verbose_name='Пик в начале')
    # TODO посмотреть че за Choices('Плавное' или 'резкое')
    # end = models.Choices(verbose_name='Окончание')
    # 'На концетрацию', 'На выносливость', 'На силу и преодоление'
    # direction_of_effect = models.Choices('Направление воздействия эффекта')
    # TODO подумать реализацию добавление трека
    # add_track = models.
    sportsman_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя спортсмена')
    photo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Фото')
    track_length = models.IntegerField(null=True, blank=True, verbose_name='Длительность трека')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'


class Coupons(models.Model):
    # TODO Привязка к id user'a
    validity_period = models.CharField(max_length=20, null=True, blank=True, verbose_name='Срок действия')
    # TODO models.Choices \/
    # status = models.Choices

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Order(models.Model):
    order_number = models.CharField(max_length=10, null=True, blank=True, verbose_name='Номер заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    # TODO Choices \/
    # status = models.Choices()
    price = models.IntegerField(null=True, blank=True, verbose_name='Стоимость')

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
