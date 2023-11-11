from django.db import models


class Station(models.Model):
    latitude = models.FloatField(null=True)  # широта
    longitude = models.FloatField(null=True)  # долгота

    name = models.CharField(max_length=200)  # Название
    number = models.CharField(max_length=20, null=True)  # Телефон
    address = models.CharField(max_length=200, null=True)  # Адрес
    description = models.TextField(null=True)  # Описание

    def __str__(self):
        return f"{self.name} (Latitude: {self.latitude}, Longitude: {self.longitude})"


class Page(models.Model):
    url = models.URLField(unique=True, null=True)  # URL страницы
    title_ru = models.CharField(max_length=200, null=False, default='default value')
    title_en = models.CharField(max_length=200, null=False, default='default value')
    content_ru = models.BooleanField(default=True)  # Булево поле для наличия контента на русском
    content_en = models.BooleanField(default=False)  # Булево поле для наличия контента на английском

    def __str__(self):
        return self.url


class Service(models.Model):
    icon_class = models.CharField(max_length=50, null=True)  # Текстовое поле для класса иконки
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Стоимость, числовое поле
    sorting_order = models.IntegerField(default=0)  # Поле для указания порядка отображения

    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True)  # Булевое поле для статуса (опубликовано или черновик)

    def __str__(self):
        return self.icon_class


class Setting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100)
    # Остальные необходимые поля можно действительно добавить сюда в зависимости от конкретных требований к настройкам.