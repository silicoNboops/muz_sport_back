from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    author = models.CharField(max_length=150, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название трека')
    sport_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Вид спорта')
    price = models.IntegerField(max_length=25, null=True, blank=True, verbose_name='Цена')
    beginning_peak = models.BooleanField(blank=True, verbose_name='Пик в начале')
    # TODO посмотреть че за Choices('Плавное' или 'резкое')
    # end = models.Choices(verbose_name='Окончание')
    # 'На концетрацию', 'На выносливость', 'На силу и преодоление'
    # direction_of_effect = models.Choices('Направление воздействия эффекта')
    # TODO подумать реализацию добавление трека
    # add_track = models.
    sportsman_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя спортсмена')
    photo = models.CharField(max_length=150, null=True, blank=True, verbose_name='Фото')
    track_length = models.IntegerField(max_length=150, null=True, blank=True, verbose_name='Длительность трека')