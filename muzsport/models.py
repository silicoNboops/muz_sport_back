from django.db import models


STATUS_CHOICES =(
    ("Active", "Активен"),
    ("Disable", "Не активен"),
)


END_CHOICES =(
    ("Smooth", "Плавное"),
    ("Sharp", "Резкое"),
)


DIRECTION_EFFECT =(
    ("Concentration", "На концетрацию"),
    ("Stamina", "На выносливость"),
    ("Force", "На силу и преодоление"),
)


ORDER_STATUS =(
    ("Performed", "Выполнен"),
    ("Process", "В обработке"),
)


class Track(models.Model):
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    sport_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Вид спорта')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    beginning_peak = models.BooleanField(default=True, verbose_name='Пик в начале')
    end = models.CharField(max_length=32, choices=END_CHOICES, verbose_name='Окончание')
    direction_of_effect = models.CharField(max_length=64, choices=DIRECTION_EFFECT,verbose_name='Направление воздействия'
                                                                                                ' эффекта')
    # TODO подумать реализацию добавление трека
    # add_track = models.
    sportsman_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя спортсмена')
    photo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Фото')
    track_length = models.IntegerField(null=True, blank=True, verbose_name='Длительность трека')

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['id']
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'


class Coupons(models.Model):
    # TODO Привязка к id user'a
    validity_period = models.CharField(max_length=20, null=True, blank=True, verbose_name='Срок действия')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Order(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=256, null=True, blank=True, verbose_name='E-Mail')
    order_number = models.AutoField(primary_key=True, verbose_name='Номер заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(max_length=64, choices=ORDER_STATUS, default='Process', verbose_name='Статус заказа')
    price = models.IntegerField(null=True, blank=True, verbose_name='Стоимость')

    def __str__(self):
        return str(self.order_number)

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
