from django.db import models
from django.urls import reverse


class Villa(models.Model):
    title = models.CharField(max_length=120, default='Вилла', null=False, verbose_name='Наименование')
    region = models.CharField(max_length=50, default='Регион', null=False, verbose_name='Регион')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    rooms_number = models.IntegerField(null=True, verbose_name='Количество комнат')
    bedrooms_number = models.IntegerField(null=True, verbose_name='Количество спален')
    bathrooms_number = models.IntegerField(null=True, verbose_name='Количество ванных комнат')
    total_area = models.FloatField(null=True, verbose_name='Общая площадь, кв. м')
    living_area = models.FloatField(null=True, verbose_name='Жилая площадь, кв. м')
    sea_distance = models.CharField(max_length=10, null=False, verbose_name='Расстояние до моря')
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительные характеристики')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')
    slug = models.SlugField(max_length=200, default=False, db_index=True)

    def __str__(self):
        return 'Вилла: ' + self.title

    def get_absolute_url(self):
        return reverse('the_villa', kwargs={'villa_id': self.pk})

    class Meta:
        verbose_name = 'Вилла'
        verbose_name_plural = 'Виллы'
        ordering = ['-price_per_day']


class Yacht(models.Model):
    title = models.CharField(max_length=120, default='Яхта', null=False, verbose_name='Наименование')
    length = models.FloatField(null=False, verbose_name='Длина, м')
    width = models.FloatField(null=False, verbose_name='Ширина, м')
    cabins_number = models.IntegerField(null=False, verbose_name='Количество кают')
    beds_number = models.IntegerField(null=False, verbose_name='Количество спальных мест')
    maximum_speed = models.FloatField(null=False, verbose_name='Максимальная скорость, узл')
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительные характеристики')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')
    slug = models.SlugField(max_length=200, default=False, db_index=True)

    def __str__(self):
        return 'Яхта: ' + self.title

    def get_absolute_url(self):
        return reverse('the_yacht', kwargs={'yacht_id': self.pk})

    class Meta:
        verbose_name = 'Яхта'
        verbose_name_plural = 'Яхты'
        ordering = ['-price_per_day']


class Vehicle(models.Model):
    title = models.CharField(max_length=120, default='Автомобиль', null=False, verbose_name='Модель')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    color = models.CharField(max_length=30, null=False, verbose_name='Цвет кузова')
    seats_number = models.IntegerField(null=False, verbose_name='Количество мест')
    doors_number = models.IntegerField(null=False, verbose_name='Количество дверей')
    horsepower = models.IntegerField(null=False, verbose_name='Мощность, л.с.')
    engine = models.FloatField(null=False, verbose_name='Объекм двигателя, куб. см')
    transmission = models.CharField(max_length=15, null=False, verbose_name='Трансмиссия')
    drive = models.CharField(max_length=15, null=False, verbose_name='Привод')
    maximum_speed = models.FloatField(null=False, verbose_name='Максимальная скорость, км/час')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('the_vehicle', kwargs={'vehicle_id': self.pk})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-price_per_day']


class VillaPhoto(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.PROTECT, null=True, verbose_name='Вилла',
                              related_name='villa_photos')
    image = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Фото виллы {self.villa.pk}'

    class Meta:
        verbose_name = 'Фото виллы'
        verbose_name_plural = 'Фотографии виллы'


class YachtPhoto(models.Model):
    yacht = models.ForeignKey(Yacht, on_delete=models.PROTECT, null=True, verbose_name='Яхта',
                              related_name='yacht_photos')
    image = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Фото яхты {self.yacht.pk}'

    class Meta:
        verbose_name = 'Фото яхты'
        verbose_name_plural = 'Фотографии яхты'


class VehiclePhoto(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, null=True, verbose_name='Автомобиль',
                                related_name='vehicle_photos')
    image = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Фото автомобиля {self.vehicle.pk}'

    class Meta:
        verbose_name = 'Фото автомобиля'
        verbose_name_plural = 'Фотографии автомобиля'
