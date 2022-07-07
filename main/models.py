from django.db import models
from simple_history.models import HistoricalRecords


class Goods(models.Model):
    name = models.CharField('Название', max_length=100)
    type = models.CharField('Тип', max_length=50)
    manufacturer = models.CharField('Производитель', max_length=200)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')
    image = models.ImageField('Изображение', upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shops = models.ManyToManyField('Shop', verbose_name='Магазины')
    history = HistoricalRecords()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
class Shop(models.Model):
    name = models.CharField('Название', max_length=100)
    location = models.CharField('Местоположение', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'